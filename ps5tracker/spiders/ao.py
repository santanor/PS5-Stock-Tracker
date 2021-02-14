import scrapy
from scrapy_splash import SplashRequest, SplashTextResponse
from twisted.internet import defer
from TrackerLog import log_stock, log_company, log_time, log_item
from ps5tracker.stockentry import StockEntry


class AOSpider(scrapy.Spider):
    name = 'AO'
    items = [
        StockEntry('Play Station 5 (Both Versions))',
                   'https://ao.com/brands/playstation',
                   '//*[@id="holder"]/div[4]/section[1]/div/div/p/strong')
    ]

    def start_requests(self):
        for i in self.items:
            deferred = defer.Deferred()
            deferred.addCallback(self.parse, i)
            yield scrapy.Request(url=i.url, callback=deferred.callback, dont_filter=True)

    def parse(self, response: SplashTextResponse, i):
        log_time()
        log_company(self.name)
        log_item(i.name)
        input = response.xpath(i.xpath).xpath('@kind').get()

        log_stock(input != 'secondary')
        print()
        return None