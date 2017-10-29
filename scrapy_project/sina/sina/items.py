# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class SinaItem(scrapy.Item):
    # 网页中的大类别标题和网址
    ptitles = scrapy.Field()
    purls = scrapy.Field()
    # 网页中的小类别标题和网址
    subtitles = scrapy.Field()
    suburls = scrapy.Field()
    # 爬取后的文件存放路径
    subpath = scrapy.Field()
    # 需要获取的内容所在的网址
    curls = scrapy.Field()
    # 爬取目标：标题和内容
    ctitles = scrapy.Field()
    contents = scrapy.Field()
