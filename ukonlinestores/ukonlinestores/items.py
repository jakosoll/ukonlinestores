# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class UkonlinestoresItem(scrapy.Item):
    seller_name = scrapy.Field()
    amazon_store = scrapy.Field()
    main_category = scrapy.Field()
    n_of_products = scrapy.Field()
    rank = scrapy.Field()
    change = scrapy.Field()
    positive_feedback = scrapy.Field()
    feedback = scrapy.Field()
    feedback_lifetime = scrapy.Field()
    fulfilment = scrapy.Field()
