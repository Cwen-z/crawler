# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
#from scrapy.spiders import CrawlSpider, Rule
from scrapy.spiders import Rule
from hongniang.items import HongniangItem
from scrapy_redis.spiders import RedisCrawlSpider

# 用RedisCrawlSpider替代原来的CrawlSpider，写注释也不容易。。。
class HongniangSpider(RedisCrawlSpider):
    name = 'hongniangSpider'
    # 这个可以不写，用init方法替代
    #allowed_domains = ['hongniang.com']
    # 改为分布式，做个标记。。
    #start_urls = ['http://www.hongniang.com/index/search?sex=2&starage=1&province=0&city=0']
    page_rule = LinkExtractor(allow=("index/search\?"))
    detail_rule = LinkExtractor(allow="user/member/id/\d+")
    # redis_key,结构通常为：类名：start_urls，启动分布式的时候需要用
    redis_key = "HongniangSpider:start_urls"
    rules = (
        Rule(page_rule),
        # Rule(page_rule,callback='parse_item',follow=True),
        Rule(detail_rule, callback='parse_item'),
    )

    # 可选：等效于allowd_domains()，__init__方法按规定格式写.
    def __init__(self, *args, **kwargs):
        Dynamically define the allowed domains list.
        domain = kwargs.pop('domain', '')
        self.allowed_domains = filter(None, domain.split(','))
    # 修改这里的类名为当前类名
        super(HongniangSpider, self).__init__(*args, **kwargs)

    def parse_item(self, response):
        #print response.url
        item = HongniangItem()
        # 昵称
        item['nickname'] = self.name_process(response)
        # id
        item['uid'] = self.uid_process(response)
        # 人物相册
        item['imageUrl'] = response.xpath("//ul[@id='tFocus-pic']//img/@src").extract()
        am = response.xpath("//div[@class='info2']/div/ul[1]/li/text()").extract()
        # 人物年龄
        item['age'] = am[0]
        # 人物婚姻状况
        item['marriage'] = am[1]
        # 人物学历
        item['education'] = response.xpath("//div[@class='info2']/div/ul[2]/li[2]/text()").extract_first()
        # 人物工作地点
        item['workingPlace'] = response.xpath("//div[@class='info2']/div/ul[3]/li[2]/text()").extract_first()
        # 人物职业
        item['occupation'] = response.xpath("//div[@class='info1'][1]//ul[1]/li[4]/text()").extract_first()
        # 人物籍贯
        item['home'] = response.xpath("//div[@class='info1'][1]//ul[2]/li[1]/text()").extract_first()
        # 择偶性别
        item['metaSex'] = response.xpath("//div[@class='info1'][4]/div[2]/ul[1]/li[1]/text()").extract_first()
        # 择偶年龄
        item['metaAge'] = response.xpath("//div[@class='info1'][4]/div[2]/ul[2]/li[1]/text()").extract_first().encode("utf-8") + '岁'
        # 择偶婚姻状况
        item['metaMarriage'] = response.xpath("//div[@class='info1'][4]/div[2]/ul[2]/li[2]/text()").extract_first()
        # 择偶工作地点
        item['metaWork'] = response.xpath("//div[@class='info1'][4]/div[2]/ul[3]/li[1]/text()").extract_first()
        # 择偶学历
        item['metaEdu'] = response.xpath("//div[@class='info1'][4]/div[2]/ul[3]/li[2]/text()").extract_first()
        yield item

    def name_process(self, response):
        name1 = response.xpath("//div[@class='name nickname']/text()").extract()
        name = "".join(name1).strip()
        return name

    def uid_process(self,response):
        uid1 = response.xpath("//div[@class='info1']//div[@class='loveid']/text()").extract_first()
        uid = uid1[7:]
        return uid

