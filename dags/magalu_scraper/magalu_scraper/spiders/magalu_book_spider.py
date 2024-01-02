import scrapy

from ..items import BookItem
from ..itemloaders import BookItemLoader

class MagaluBookSpider(scrapy.Spider) :
    name = 'magalu_book'
    start_urls = [
        'https://www.magazineluiza.com.br/livros/l/li/',
    ]
    
    book_strs = {
        'title': 'Título',
        'publisher': 'Editora',
        'isbn': 'Referência',
        'subtitle': 'Subtítulo',
        'author': 'Autor',
        'genre': 'Classificação',
        'year': 'Ano de publicação',
        'number_pages': 'Número de páginas',
        'language': 'Idioma'
    }
    
    def parse(self, response) :
        book_links = response.xpath('//li[@class="sc-APcvf eJDyHN"]//a/@href')

        yield from response.follow_all(book_links[:10], self.parse_book)

        yield from self.parse_book(response)
            
    def parse_book(self, response) :
        loader = BookItemLoader(selector=response)

        loader.add_value('url', response.url)
        loader.add_xpath('product_title', '//*[@data-testid="heading-product-title"]/text()')
        loader.add_xpath('product_description', '//div[@data-testid="product-detail-description"]//text()')
        
        loader.add_xpath('product_price_original', '//p[@data-testid="price-value"]//text()')
        loader.add_xpath('product_price_current', '//p[@data-testid="price-original"]//text()')

        main_table_loader = loader.nested_xpath('//table[@class="sc-fqkvVR dUvaSJ sc-rPWID dHZzuS"]/tbody/tr')

        main_table_loader.add_xpath('title', '.' + self.get_table_value_by_key(self.book_strs['title']) + '//text()')
        main_table_loader.add_xpath('subtitle', '.' + self.get_table_value_by_key(self.book_strs['subtitle']) + '//text()')
        main_table_loader.add_xpath('isbn', '.' + self.get_table_value_by_key(self.book_strs['isbn']) + '//text()')
        main_table_loader.add_xpath('publisher', '.' + self.get_table_value_by_key(self.book_strs['publisher']) + '//text()')
        main_table_loader.add_xpath('author', '.' + self.get_table_value_by_key(self.book_strs['author']) + '//text()')
        main_table_loader.add_xpath('genre', '.' + self.get_table_value_by_key(self.book_strs['genre']) + '//text()')
        main_table_loader.add_xpath('year', '.' + self.get_table_value_by_key(self.book_strs['year']) + '//text()')
        main_table_loader.add_xpath('number_pages', '.' + self.get_table_value_by_key(self.book_strs['number_pages']) + '//text()')
        main_table_loader.add_xpath('language', '.' + self.get_table_value_by_key(self.book_strs['language']) + '//text()')

        technical_info_table_loader = main_table_loader.nested_xpath('.' + self.get_table_value_by_key('Informações técnicas'))
        technical_info_table_loader.add_xpath('title', './' + self.get_table_value_by_key(self.book_strs['title']) + '//text()')
        technical_info_table_loader.add_xpath('publisher', './' + self.get_table_value_by_key(self.book_strs['publisher']) + '//text()')
        
        product_sheet_table_loader = main_table_loader.nested_xpath('.' + self.get_table_value_by_key('Ficha técnica'))
        product_sheet_table_loader.add_xpath('number_pages', './' + self.get_table_value_by_key(self.book_strs['number_pages']) + '//text()')
        product_sheet_table_loader.add_xpath('language', './' + self.get_table_value_by_key(self.book_strs['language']) + '//text()')

        yield loader.load_item()        
        
    def get_table_value_by_key(self, key) :
        return f'/td[1][.="{key}"]/following-sibling::*'