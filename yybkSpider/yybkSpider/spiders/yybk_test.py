import scrapy


class YybkTestSpider(scrapy.Spider):
    name = 'yybk_test'
    allowed_domains = ['yunyubaike.com']
    start_urls = ['http://yunyubaike.com/']

    def parse(self, response):
        pass
