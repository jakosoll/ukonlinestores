import scrapy
import json
from scrapy.shell import inspect_response




class MainSpider(scrapy.Spider):
    def __init__(self, *args, **kwargs):
        self.infile = kwargs.pop('inputfile')

    name = 'main'
    allowed_domains = ['ukonlinestores.co.uk']
    start_urls = ['https://ukonlinestores.co.uk/']
    search_url = 'https://ukonlinestores.co.uk/wp-admin/admin-ajax.php?action=get_wdtable&table_id=9'
    handle_httpstatus_list = [400]

    def parse_search(self, response):
        # data = json.loads(response.text)
        inspect_response(response, self)
        # item = UkonlinestoresItem()
        # list_data = data["date"]
        # for i in range(len(data["date"])):
        #     item['seller_name'] = list_data[2]
        #     print(item['seller_name'])

    def parse(self, response):
        headers = {
            "accept": "application/json, text/javascript, */*; q=0.01",
            "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
            "content-type": "application/json;charset=UTF-8",
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin"
        }


        yield scrapy.Request(self.search_url, callback=self.parse_search, method='POST', body=json.dumps(self.infile),
                             headers=headers)

