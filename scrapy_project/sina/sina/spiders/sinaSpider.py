# -*- coding: utf-8 -*-
import scrapy
import os
from sina.items import SinaItem

class SinaspiderSpider(scrapy.Spider):
    name = "sinaSpider"
    allowed_domains = ["sina.com.cn"]
    start_urls = (
        'http://news.sina.com.cn/guide/',
    )

    def parse(self, response):
        purls = response.xpath("//div[@id='tab01']/div/h3/a/@href").extract()
        ptitles = response.xpath("//div[@id='tab01']/div/h3/a/text()").extract()

        subtitles = response.xpath("//div[@id='tab01']/div//li/a/text()").extract()
        suburls = response.xpath("//div[@id='tab01']/div//li/a/@href").extract()

        for i in range(0,len(ptitles)):
            pfilename = "./SinaData/" + ptitles[i]
            if (not os.path.exists(pfilename)):
                os.makedirs(pfilename)
            for j in range(0,len(suburls)):
                urls_belong = suburls[j].startswith(purls[i])
                if urls_belong:
                    subpath = pfilename + "/" + subtitles[j]
                    if (not os.path.exists(subpath)):
                        os.makedirs(subpath)
                    item = SinaItem()
                    item['ptitles'] = ptitles[i]
                    item['purls'] = purls[i]
                    item['subtitles'] = subtitles[j]
                    item['suburls'] = suburls[j]
                    item['subpath'] = subpath
                    yield scrapy.Request(url = item['suburls'], meta = {'meta_1':item}, callback=self.subparse)


    def subparse(self, response):
        item1 = response.meta['meta_1']
        # cpaths = response.xpath("//div[contains(@class,'news-list')]//a")
        curls = response.xpath("//a/@href").extract()
        # ctitles = //div[contains(@class,'news-list')]//a/@href
        for k in range(0, len(curls)):
            curls_belong = curls[k].endswith(".shtml") and curls[k].startswith(item1['purls'])
            if (curls_belong):
                item = SinaItem()
                item['ptitles'] = item1['ptitles']
                item['purls'] = item1['purls']
                item['subtitles'] = item1['subtitles']
                item['suburls'] = item1['suburls']
                item['subpath'] = item1['subpath']
                item['curls'] = curls[k]
                yield scrapy.Request(url = item['curls'], meta = {'meta_2':item}, callback = self.contentparse)

    def contentparse(self, response):
        item = response.meta['meta_2']
        ctitle = response.xpath("//h1[contains(@id,'itle')]/text()").extract()
        content = response.xpath("//div[@id='artibody']/p/text()").extract()
        ctitles = "".join(ctitle)
        contents = "\n".join(content)
        item['ctitles'] = ctitles
        item['contents'] = contents
        yield item
