# -*- coding: utf-8 -*-
import scrapy
import os
from scrapy.utils.project import get_project_settings
from scrapy.pipelines.images import ImagesPipeline
from settings import IMAGES_STORE


class DouyuPipeline(ImagesPipeline):
    # IMAGES_STORE = get_project_settings().get("IMAGES_STORE")
    def get_media_requests(self, item, info):
        image_url = item['imagesUrls']
        yield scrapy.Request(image_url)

    def item_completed(self, results, item, info):
        image_path = [x['path'] for ok, x in results if ok]
        os.rename(IMAGES_STORE + "/" + image_path[0], IMAGES_STORE + "/" + item["name"] + ".jpg")
        item['imagesPath'] = IMAGES_STORE + '/' + item['name']
        return item
