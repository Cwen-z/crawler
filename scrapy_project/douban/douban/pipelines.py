# -*- coding: utf-8 -*-
import  pymongo
from scrapy.conf import settings
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class DoubanPipeline(object):
    def __init__(self):
        host = settings["MONGODB_HOST"]
        port = settings["MONGODB_PORT"]
        dbname = settings["MONGODB_DBNAME"]
        sheetname = settings["MONGODB_SHEETNAME"]
        conn = pymongo.MongoClient(host, port)
        db = conn[dbname]
        self.sheet = db[sheetname]

    def process_item(self, item, spider):
        data = dict(item)
        self.sheet.insert(data)
        return item
