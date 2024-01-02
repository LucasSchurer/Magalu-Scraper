# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class BookItem(scrapy.Item) :
    url = scrapy.Field()
    
    product_title = scrapy.Field()
    product_dimensions = scrapy.Field()
    product_weight = scrapy.Field()
    product_warranty = scrapy.Field()
    product_description = scrapy.Field()

    product_price_original = scrapy.Field()
    product_price_current = scrapy.Field()
    
    publisher = scrapy.Field()
    title = scrapy.Field()
    subtitle = scrapy.Field()
    isbn = scrapy.Field()
    author = scrapy.Field()
    genre = scrapy.Field()
    year = scrapy.Field()
    number_pages = scrapy.Field()
    language = scrapy.Field()

    pass