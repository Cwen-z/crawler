# -*- coding: utf-8 -*-
import json
import codecs
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class DongguanPipeline(object):
    def __init__(self):
        self.filename = codecs.open("dongguan_sun.json", "w", encoding="utf-8")

    def process_item(self, item, spider):
        sun_file = json.dumps(dict(item), ensure_ascii=False)
        self.filename.write(sun_file + "\n")

    def close_spider(self):
        self.filename.close()
