from itemloaders.processors import TakeFirst, Compose, Join, MapCompose
from scrapy.loader import ItemLoader
from .items import BookItem

def remove_currency_symbol(value) :
    value = value.replace('R$', '')
    value = value.replace(' ', '')
    value = value.encode('ascii', 'ignore')
    value = value.decode()

    return value

class BookItemLoader(ItemLoader) :
    default_item_class = BookItem
    default_output_processor = TakeFirst()

    isbn_in = MapCompose(lambda x: x.replace('-', ''))
    product_price_current_in = MapCompose(remove_currency_symbol)
    product_price_original_in = MapCompose(remove_currency_symbol)