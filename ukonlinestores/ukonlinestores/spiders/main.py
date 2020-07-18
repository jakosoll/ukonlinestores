import scrapy
import json


from ..items import UkonlinestoresItem
import time

class MainSpider(scrapy.Spider):
    name = 'main'
    allowed_domains = ['ukonlinestores.co.uk']
    start_urls = ['https://ukonlinestores.co.uk/amazon-uk-sellers/']
    search_url = 'https://ukonlinestores.co.uk/wp-admin/admin-ajax.php?action=get_wdtable&table_id=9'
    handle_httpstatus_list = [400]

    def parse_search(self, response):
        data = json.loads(response.body)['data']
        # inspect_response(response, self)
        item = UkonlinestoresItem()

        for line in data:
            item['seller_name'] = line[1]
            item['amazon_store'] = line[2].split()[1].lstrip('href=').strip('\'')
            item['main_category'] = line[4]
            item['n_of_products'] = line[5]
            item['rank'] = line[6]
            item['change'] = line[7]
            item['positive_feedback'] = line[10]
            item['feedback'] = line[14]
            item['feedback_lifetime'] = line[15]
            item['fulfilment'] = line[16]
            # print(item['seller_name'])
            yield item

    def parse(self, response):
        headers = {
            "authority": "ukonlinestores.co.uk",
            "accept": "application/json, text/javascript, */*; q=0.01",
            "dnt": "1",
            "x-requested-with": "XMLHttpRequest",
            "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36",
            "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
            "origin": "https://ukonlinestores.co.uk",
            "sec-fetch-site": "same-origin",
            "sec-fetch-mode": "cors",
            "sec-fetch-dest": "empty",
            "referer": "https://ukonlinestores.co.uk/amazon-uk-sellers/",
            "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7"
        }

        cookies = {
            "_ga": "GA1.3.1327773904.1594840444",
            " _gid": "GA1.3.1108160461.1594840444",
            " _gat": "1",
            " _gat_gtag_UA_111791420_1": "1"
        }

        id_parse = response.xpath('//*[@id="wdtNonceFrontendEdit"]/@value').extract()[0]

        body = 'draw=3&columns%5B0%5D%5Bdata%5D=0&columns%5B0%5D%5Bname%5D=wdt_ID&columns%5B0%5D%5Bsearchable%5D' \
               '=true&columns%5B0%5D%5Borderable%5D=true&columns%5B0%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B0%5D' \
               '%5Bsearch%5D%5Bregex%5D=false&columns%5B1%5D%5Bdata%5D=1&columns%5B1%5D%5Bname%5D=sellerid&columns' \
               '%5B1%5D%5Bsearchable%5D=true&columns%5B1%5D%5Borderable%5D=true&columns%5B1%5D%5Bsearch%5D%5Bvalue' \
               '%5D=&columns%5B1%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B2%5D%5Bdata%5D=2&columns%5B2%5D%5Bname%5D' \
               '=storefronturl&columns%5B2%5D%5Bsearchable%5D=true&columns%5B2%5D%5Borderable%5D=false&columns%5B2' \
               '%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B2%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B3%5D%5Bdata%5D=3' \
               '&columns%5B3%5D%5Bname%5D=sellername&columns%5B3%5D%5Bsearchable%5D=true&columns%5B3%5D%5Borderable' \
               '%5D=true&columns%5B3%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B3%5D%5Bsearch%5D%5Bregex%5D=false&columns' \
               '%5B4%5D%5Bdata%5D=4&columns%5B4%5D%5Bname%5D=maincategory&columns%5B4%5D%5Bsearchable%5D=true' \
               '&columns%5B4%5D%5Borderable%5D=true&columns%5B4%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B4%5D%5Bsearch' \
               '%5D%5Bregex%5D=false&columns%5B5%5D%5Bdata%5D=5&columns%5B5%5D%5Bname%5D=noofproducts&columns%5B5%5D' \
               '%5Bsearchable%5D=true&columns%5B5%5D%5Borderable%5D=true&columns%5B5%5D%5Bsearch%5D%5Bvalue%5D' \
               '=&columns%5B5%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B6%5D%5Bdata%5D=6&columns%5B6%5D%5Bname%5D' \
               '=rank&columns%5B6%5D%5Bsearchable%5D=true&columns%5B6%5D%5Borderable%5D=true&columns%5B6%5D%5Bsearch' \
               '%5D%5Bvalue%5D=&columns%5B6%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B7%5D%5Bdata%5D=7&columns%5B7' \
               '%5D%5Bname%5D=change&columns%5B7%5D%5Bsearchable%5D=true&columns%5B7%5D%5Borderable%5D=false&columns' \
               '%5B7%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B7%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B8%5D%5Bdata%5D' \
               '=8&columns%5B8%5D%5Bname%5D=positive30day&columns%5B8%5D%5Bsearchable%5D=true&columns%5B8%5D' \
               '%5Borderable%5D=true&columns%5B8%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B8%5D%5Bsearch%5D%5Bregex%5D' \
               '=false&columns%5B9%5D%5Bdata%5D=9&columns%5B9%5D%5Bname%5D=positive90day&columns%5B9%5D%5Bsearchable' \
               '%5D=true&columns%5B9%5D%5Borderable%5D=true&columns%5B9%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B9%5D' \
               '%5Bsearch%5D%5Bregex%5D=false&columns%5B10%5D%5Bdata%5D=10&columns%5B10%5D%5Bname%5D' \
               '=positive12months&columns%5B10%5D%5Bsearchable%5D=true&columns%5B10%5D%5Borderable%5D=true&columns' \
               '%5B10%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B10%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B11%5D%5Bdata' \
               '%5D=11&columns%5B11%5D%5Bname%5D=positivelifetime&columns%5B11%5D%5Bsearchable%5D=true&columns%5B11' \
               '%5D%5Borderable%5D=true&columns%5B11%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B11%5D%5Bsearch%5D%5Bregex' \
               '%5D=false&columns%5B12%5D%5Bdata%5D=12&columns%5B12%5D%5Bname%5D=count30day&columns%5B12%5D' \
               '%5Bsearchable%5D=true&columns%5B12%5D%5Borderable%5D=true&columns%5B12%5D%5Bsearch%5D%5Bvalue%5D' \
               '=&columns%5B12%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B13%5D%5Bdata%5D=13&columns%5B13%5D%5Bname' \
               '%5D=count90day&columns%5B13%5D%5Bsearchable%5D=true&columns%5B13%5D%5Borderable%5D=true&columns%5B13' \
               '%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B13%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B14%5D%5Bdata%5D' \
               '=14&columns%5B14%5D%5Bname%5D=count12months&columns%5B14%5D%5Bsearchable%5D=true&columns%5B14%5D' \
               '%5Borderable%5D=true&columns%5B14%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B14%5D%5Bsearch%5D%5Bregex%5D' \
               '=false&columns%5B15%5D%5Bdata%5D=15&columns%5B15%5D%5Bname%5D=countlifetime&columns%5B15%5D' \
               '%5Bsearchable%5D=true&columns%5B15%5D%5Borderable%5D=true&columns%5B15%5D%5Bsearch%5D%5Bvalue%5D' \
               '=&columns%5B15%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B16%5D%5Bdata%5D=16&columns%5B16%5D%5Bname' \
               '%5D=fulfilmenttype1&columns%5B16%5D%5Bsearchable%5D=true&columns%5B16%5D%5Borderable%5D=true&columns' \
               '%5B16%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B16%5D%5Bsearch%5D%5Bregex%5D=false&order%5B0%5D%5Bcolumn' \
               '%5D=6&order%5B0%5D%5Bdir%5D=asc&start={}&length=50&search%5Bvalue%5D=&search%5Bregex%5D=false' \
               '&wdtNonce={}&sRangeSeparator=%7C '

        for i in range(1339):
            yield scrapy.Request(url=self.search_url, callback=self.parse_search, method='POST', headers=headers, body=body.format(i*10, id_parse), cookies=cookies, dont_filter=True)

