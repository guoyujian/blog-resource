# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class YybkspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class YybkspiderListItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    this_url = scrapy.Field()
    page_num = scrapy.Field()
    count = scrapy.Field()
    detail_url = scrapy.Field()
    title = scrapy.Field()
    pass
