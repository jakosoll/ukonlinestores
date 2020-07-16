import scrapy
import json
from scrapy.shell import inspect_response


class MainSpider(scrapy.Spider):
    name = 'main'
    allowed_domains = ['ukonlinestores.co.uk']
    # start_urls = ['https://ukonlinestores.co.uk/amazon-uk-sellers/']
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

    def start_requests(self):
        headers = {
            'authority': 'ukonlinestores.co.uk',
            'accept': 'application/json, text/javascript, */*; q=0.01',
            'dnt': '1',
            'x-requested-with': 'XMLHttpRequest',
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36',
            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'origin': 'https://ukonlinestores.co.uk',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-mode': 'cors',
            'sec-fetch-dest': 'empty',
            'referer': 'https://ukonlinestores.co.uk/amazon-uk-sellers/',
            'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
            'cookie': '_ga=GA1.3.1327773904.1594840444; _gid=GA1.3.1108160461.1594840444; _gat=1; _gat_gtag_UA_111791420_1=1',
        }

        params = {
            'action': 'get_wdtable',
            'table_id': '21',
        }

        cookies = {
            '_ga': 'GA1.3.1327773904.1594840444',
            '_gid': 'GA1.3.1108160461.1594840444',
            'gat': '1',
            '_gat_gtag_UA_111791420_1': '1',
        }

        data = {
            'draw': '2',
            'columns[0][data]': '0',
            'columns[0][name]': 'wdt_ID',
            'columns[0][searchable]': 'true',
            'columns[0][orderable]': 'true',
            'columns[0][search][value]': '',
            'columns[0][search][regex]': 'false',
            'columns[1][data]': '1',
            'columns[1][name]': 'sellerid',
            'columns[1][searchable]': 'true',
            'columns[1][orderable]': 'true',
            'columns[1][search][value]': '',
            'columns[1][search][regex]': 'false',
            'columns[2][data]': '2',
            'columns[2][name]': 'storefronturl',
            'columns[2][searchable]': 'true',
            'columns[2][orderable]': 'false',
            'columns[2][search][value]': '',
            'columns[2][search][regex]': 'false',
            'columns[3][data]': '3',
            'columns[3][name]': 'sellername',
            'columns[3][searchable]': 'true',
            'columns[3][orderable]': 'true',
            'columns[3][search][value]': '',
            'columns[3][search][regex]': 'false',
            'columns[4][data]': '4',
            'columns[4][name]': 'maincategory',
            'columns[4][searchable]': 'true',
            'columns[4][orderable]': 'true',
            'columns[4][search][value]': '',
            'columns[4][search][regex]': 'false',
            'columns[5][data]': '5',
            'columns[5][name]': 'noofproducts',
            'columns[5][searchable]': 'true',
            'columns[5][orderable]': 'true',
            'columns[5][search][value]': '',
            'columns[5][search][regex]': 'false',
            'columns[6][data]': '6',
            'columns[6][name]': 'rank',
            'columns[6][searchable]': 'true',
            'columns[6][orderable]': 'true',
            'columns[6][search][value]': '',
            'columns[6][search][regex]': 'false',
            'columns[7][data]': '7',
            'columns[7][name]': 'change',
            'columns[7][searchable]': 'true',
            'columns[7][orderable]': 'false',
            'columns[7][search][value]': '',
            'columns[7][search][regex]': 'false',
            'columns[8][data]': '8',
            'columns[8][name]': 'positive30day',
            'columns[8][searchable]': 'true',
            'columns[8][orderable]': 'true',
            'columns[8][search][value]': '',
            'columns[8][search][regex]': 'false',
            'columns[9][data]': '9',
            'columns[9][name]': 'positive90day',
            'columns[9][searchable]': 'true',
            'columns[9][orderable]': 'true',
            'columns[9][search][value]': '',
            'columns[9][search][regex]': 'false',
            'columns[10][data]': '10',
            'columns[10][name]': 'positive12months',
            'columns[10][searchable]': 'true',
            'columns[10][orderable]': 'true',
            'columns[10][search][value]': '',
            'columns[10][search][regex]': 'false',
            'columns[11][data]': '11',
            'columns[11][name]': 'positivelifetime',
            'columns[11][searchable]': 'true',
            'columns[11][orderable]': 'true',
            'columns[11][search][value]': '',
            'columns[11][search][regex]': 'false',
            'columns[12][data]': '12',
            'columns[12][name]': 'count30day',
            'columns[12][searchable]': 'true',
            'columns[12][orderable]': 'true',
            'columns[12][search][value]': '',
            'columns[12][search][regex]': 'false',
            'columns[13][data]': '13',
            'columns[13][name]': 'count90day',
            'columns[13][searchable]': 'true',
            'columns[13][orderable]': 'true',
            'columns[13][search][value]': '',
            'columns[13][search][regex]': 'false',
            'columns[14][data]': '14',
            'columns[14][name]': 'count12months',
            'columns[14][searchable]': 'true',
            'columns[14][orderable]': 'true',
            'columns[14][search][value]': '',
            'columns[14][search][regex]': 'false',
            'columns[15][data]': '15',
            'columns[15][name]': 'countlifetime',
            'columns[15][searchable]': 'true',
            'columns[15][orderable]': 'true',
            'columns[15][search][value]': '',
            'columns[15][search][regex]': 'false',
            'columns[16][data]': '16',
            'columns[16][name]': 'fulfilmenttype1',
            'columns[16][searchable]': 'true',
            'columns[16][orderable]': 'true',
            'columns[16][search][value]': '',
            'columns[16][search][regex]': 'false',
            'order[0][column]': '6',
            'order[0][dir]': 'asc',
            'start': '0',
            'length': '10',
            'search[value]': '',
            'search[regex]': 'false',
            'wdtNonce': 'fe41c4c9f5',
            'sRangeSeparator': '|',
        }
        yield scrapy.Request(self.search_url, callback=self.parse_search, method='POST', body=json.dumps(data))

