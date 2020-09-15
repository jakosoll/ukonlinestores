import scrapy


class YmapsSpider(scrapy.Spider):
    name = 'ymaps'
    allowed_domains = ['yandex.ru']
    start_urls = ['http://yandex.ru/maps/api/search?']
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:80.0) Gecko/20100101 Firefox/80.0',
        'Accept': '*/*',
        'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
        'Accept-Encoding': 'gzip, deflate, br'
    }

    def parse_search(self, response):
        items = response.json.get('data').get('items')


    def parse(self, response):
        resp_dict = response.json()
        csrf = resp_dict.get('csrfToken')
        ctx = resp_dict.get('ctx')
        result = 100
        ya_urls = 'https://yandex.ru/maps/api/search?add_type=direct&ajax=1&csrfToken' \
                  f'={csrf}&ctx={ctx}&direct_page_id=242&lang=ru_RU&origin=maps-scroll' \
                  f'&parent_reqid=1600159663166922-2556406911-sas1-6222-sas-addrs-nmeta-new-8031&results={result}&s' \
                  '=3683772580&serpid=1600159663166922-2556406911-sas1-6222-sas-addrs-nmeta-new-8031&sessionId' \
                  '=1600159651738_363230&skip=25&snippets=masstransit/2.x,panoramas/1.x,businessrating/1.x,' \
                  'businessimages/1.x,photos/2.x,fuel/1.x,realty_experimental/2.x,experimental/1.x,subtitle/1.x,' \
                  'exchange/1.x,matchedobjects/1.x,discovery/1.x,visits_histogram/2.x,topobjects/1.x,showtimes/1.x,' \
                  'promo_mastercard/1.x:mastercardoffers,tycoon_owners_personal/1.x,tycoon_posts/1.x,' \
                  'related_adverts/1.x,related_adverts_1org/1.x,route_point/1.x,topplaces/1.x,metrika_snippets/1.x,' \
                  'afisha_json_geozen/1.x,place_summary/1.x,encyclopedia/1.x,online_snippets/1.x,' \
                  'building_info_experimental/1.x,provider_data/1.x&test-buckets=182560,0,19;278491,0,71;45970,0,' \
                  '56;278820,0,23;272652,0,38;278546,0,34;275109,0,74;278351,0,94;278561,0,40;89889,0,15;221191,0,' \
                  '20;271746,0,30;272589,0,20;204309,0,38;278787,0,25;135541,0,25;274973,0,51;271613,0,35;277815,0,' \
                  '53&text={"text":"hospital","what":[{"attr_name":"rubric","attr_values":[' \
                  '"hospital"]}]}&yandex_gid=35 '
        return scrapy.Request(url=ya_urls, callback=self.parse_search, method='GET', headers=self.headers,)
