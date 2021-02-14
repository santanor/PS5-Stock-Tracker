import scrapy
from scrapy_splash import SplashRequest, SplashTextResponse
from twisted.internet import defer
from TrackerLog import log_stock, log_company, log_time, log_item
from ps5tracker.stockentry import StockEntry


class GameSpider(scrapy.Spider):
    name = 'Game'
    items = [
        StockEntry('Play Station 5 Disc Edition',
                   'https://www.game.co.uk/playstation-5',
                   '//*[@id="contentPanels3"]/div/div/div[1]/span/a'),
        StockEntry('Play Station 5 Console Edition',
                   'https://www.game.co.uk/playstation-5',
                   '//*[@id="contentPanels3"]/div/div/div[2]/span/a')
    ]
    xpath = "/html/body/div[7]/section/div/div/div[2]/div[1]/div[6]/div/div/div/div[1]/div[1]/div[1]/div/label/input"

    def start_requests(self):
        for i in self.items:
            deferred = defer.Deferred()
            deferred.addCallback(self.parse, i)
            yield SplashRequest(url=i.url, callback=deferred.callback, dont_filter=True)

    def parse(self, response: SplashTextResponse, i):
        log_time()
        log_company(self.name)
        log_item(i.name)
        input = response.xpath(i.xpath)
        disabled_value = input.xpath('./text()').get()

        log_stock(disabled_value != 'Out of stock')
        print()
        return None
