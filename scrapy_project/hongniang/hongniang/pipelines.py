# -*- coding: utf-8 -*-
import codecs
import json
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class HongniangPipeline(object):
    def __init__(self):
        self.filename = codecs.open("hongniang1.json", 'w', encoding="utf-8")

    def process_item(self, item, spider):
        fp = json.dumps(dict(item), ensure_ascii=False)
        self.filename.write(fp + '\n')
        return item

    def close_spider(self, spider):
        self.filename.close()

