import scrapy
from twisted.internet import defer
from TrackerLog import log_stock, log_company, log_time, log_item
from ps5tracker.stockentry import StockEntry


class SmythsSpider(scrapy.Spider):
    name = 'Smyth Toys'
    items = [
        StockEntry('Play Station 5 Disc Edition',
                   'https://www.smythstoys.com/uk/en-gb/video-games-and-tablets/playstation-5/playstation-5-consoles/playstation-5-console/p/191259/',
                   "/html/body/div[7]/section/div/div/div[2]/div[1]/div[6]/div/div/div/div[1]/div[1]/div[1]/div/label/input"),
        StockEntry('Play Station 5 Digital Edition',
                   'https://www.smythstoys.com/uk/en-gb/video-games-and-tablets/playstation-5/playstation-5-consoles/playstation-5-digital-edition-console/p/191430',
                   "/html/body/div[7]/section/div/div/div[2]/div[1]/div[6]/div/div/div/div[1]/div[1]/div[1]/div/label/input")
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
        input = response.xpath(i.xpath)
        disabledValue = input.xpath('//input/@disabled').get()

        log_stock(disabledValue != 'disabled')
        print()
        return None
