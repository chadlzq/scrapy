# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.pipelines.images import ImagesPipeline
import scrapy

class WallpaperPipeline(object):
    def process_item(self, item, spider):
        return item

class WallpaperImagePipeline(ImagesPipeline):
    def get_media_requests(self,item,info):
        yield scrapy.Request(url=item['src'],meta={'item':item})

    def file_path(self,request,response=None,info=None):
        item = request.meta['item']
        path = item['src'].split('/')[-1]
        if '.' in path:
            path = path.split('.')[0]
        return path


    
