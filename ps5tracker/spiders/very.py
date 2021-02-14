import scrapy
from twisted.internet import defer
from TrackerLog import log_stock, log_company, log_time, log_item
from ps5tracker.stockentry import StockEntry


class VerySpider(scrapy.Spider):
    name = 'Very'
    items = [
        StockEntry('Play Station 5 (Both Editions)',
                   'https://www.very.co.uk/playstation-5-sign-up.page',
                   '//*[@id="lpContainer"]/comment()[1]')
    ]

    def start_requests(self):
        for i in self.items:
            deferred = defer.Deferred()
            deferred.addCallback(self.parse, i)
            yield scrapy.Request(url=i.url, callback=deferred.callback)

    def parse(self, response, i):
        log_time()
        log_company(self.name)
        log_item(i.name)
        input = response.xpath(i.xpath).get()
        log_stock(input != '<!-- <a class="bsCell bsCell--header margin64" href="/web/en/emailSubscription.page" title="PS5 - Register your interest"> -->')
        print()
        return None
