# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class WorshopScrapingItem(scrapy.Item):
    name = scrapy.Field()
    description = scrapy.Field()
    id = scrapy.Field()
    current_url = scrapy.Field()
    image = scrapy.Field()
    detail_link = scrapy.Field()
    price = scrapy.Field()
    old_price = scrapy.Field()
    availability = scrapy.Field()
    flag = scrapy.Field()
    pass
