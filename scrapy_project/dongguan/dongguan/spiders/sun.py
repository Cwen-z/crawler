# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf8')
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from dongguan.items import DongguanItem

class SunSpider(CrawlSpider):
    name = 'sun'
    allowed_domains = ['wz.sun0769.com']
    start_urls = ['http://wz.sun0769.com/index.php/question/questionType?type=4&page=0']
    page_links = LinkExtractor(allow=r"type=4")
    content_links = LinkExtractor(allow=r"html/question/\d+/\d+.shtml")
    rules = (
        Rule(page_links),  # 没有回调函数，follow默认为True，否则为False
        Rule(content_links, callback='parse_item', follow=False)
    )

    def parse_item(self, response):
        print response.url
        item = DongguanItem()
        title = response.xpath("//div[@class='pagecenter p3']//strong/text()").extract()[0]
        item['title'] = title.split(u"：")[-1].split(":")[0][:-2]
        item['url'] = response.url
        item['number'] = title.split(":")[-1]
        content = response.xpath("//div[@class='contentext']/text()").extract()
        if len(content) == 0:
            item['content'] = " ".join(response.xpath("//div[@class='c1 text14_2']/text()").extract()).strip()
        else:
            item['content'] = " ".join(content).strip()

        yield item




