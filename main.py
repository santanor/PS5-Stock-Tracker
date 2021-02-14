from scrapy.utils import defer, reactor
from scrapy.utils.project import get_project_settings
from ps5tracker.spiders.game import GameSpider
from ps5tracker.spiders.smyths import SmythsSpider
from ps5tracker.spiders.very import VerySpider
from ps5tracker.spiders.argos import ArgosSpider
from ps5tracker.spiders.ao import AOSpider

from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from twisted.internet import reactor
from twisted.internet.task import deferLater


def sleep(self, *args, seconds):
    """Non blocking sleep callback"""
    return deferLater(reactor, seconds, lambda: None)


def _crawl(result, spider):
    deferred = process.crawl(spider)
    deferred.addCallback(sleep, seconds=5)
    deferred.addCallback(_crawl, spider)
    return deferred


settings = get_project_settings()
process = CrawlerProcess(settings)

#_crawl(None, SmythsSpider)
#_crawl(None, GameSpider)
#_crawl(None, VerySpider)
#_crawl(None, ArgosSpider)
_crawl(None, AOSpider)

process.start()
