# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class SinaPipeline(object):
    def process_item(self, item, spider):
        filename = item['ctitles'] + '.txt'
        fp = open(item['subpath'] + '/' + filename, 'w')
        fp.write(item['contents'].encode("utf-8"))
        fp.close()
        return item
