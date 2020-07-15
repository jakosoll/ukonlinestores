import scrapy


class MainSpider(scrapy.Spider):
    name = 'main'
    allowed_domains = ['https://ukonlinestores.co.uk/amazon-uk-sellers/']
    start_urls = ['http://https://ukonlinestores.co.uk/amazon-uk-sellers//']

    def parse(self, response):
        pass
