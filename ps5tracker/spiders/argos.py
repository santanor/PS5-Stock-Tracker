import scrapy
from scrapy_splash import SplashRequest, SplashTextResponse
from twisted.internet import defer
from TrackerLog import log_stock, log_company, log_time, log_item
from ps5tracker.stockentry import StockEntry


class ArgosSpider(scrapy.Spider):
    name = 'Argos'
    items = [
        StockEntry('Play Station 5 Disc Edition',
                   'https://www.argos.co.uk/search/playstation-5-console/',
                   '//*[@id="findability"]/div/div[6]/div/div[5]/div[3]/div[1]/div[2]/a'),
        StockEntry('Play Station 5 Digital Edition',
                   'https://www.argos.co.uk/search/playstation-5-console/',
                   '//*[@id="findability"]/div/div[6]/div/div[5]/div[3]/div[2]/div[2]/a')
    ]

    def start_requests(self):
        for i in self.items:
            deferred = defer.Deferred()
            deferred.addCallback(self.parse, i)
            yield SplashRequest(url=i.url, callback=deferred.callback, dont_filter=True)

    def parse(self, response: SplashTextResponse, i):
        log_time()
        log_company(self.name)
        log_item(i.name)
        input = response.xpath(i.xpath).xpath('@kind').get()

        log_stock(input != 'secondary')
        print()
        return None