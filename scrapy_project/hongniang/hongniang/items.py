# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy import Field


class HongniangItem(scrapy.Item):
    # 昵称
    nickname = Field()
    # id
    uid = Field()
    # 人物相册
    imageUrl = Field()
    # 人物年龄
    age = Field()
    # 人物婚姻状况
    marriage = Field()
    # 人物学历
    education = Field()
    # 人物工作地点
    workingPlace = Field()
    # 人物职业
    occupation = Field()
    # 人物籍贯
    home = Field()
    # 择偶性别
    metaSex = Field()
    # 择偶年龄
    metaAge = Field()
    # 择偶婚姻状况
    metaMarriage = Field()
    # 择偶工作地点
    metaWork = Field()
    # 择偶学历
    metaEdu = Field()

