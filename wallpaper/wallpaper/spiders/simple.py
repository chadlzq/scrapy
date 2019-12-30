# -*- coding: utf-8 -*-
import scrapy
from wallpaper.items import WallpaperItem
from urllib.parse import urljoin

class SimpleSpider(scrapy.Spider):
    name = 'simple'
    allowed_domains = ['simpledesktops.com']
    start_urls = [
        'http://simpledesktops.com/browse/',
        'http://simpledesktops.com/browse/2',
        'http://simpledesktops.com/browse/3',
        'http://simpledesktops.com/browse/4',
        'http://simpledesktops.com/browse/5',
        'http://simpledesktops.com/browse/6',
        'http://simpledesktops.com/browse/7',
        'http://simpledesktops.com/browse/8',
        ]

    def parse(self, response):
        href_list = response.xpath('//div[@class="desktop"]/a/@href').extract()
        for href in href_list:
            yield scrapy.Request(urljoin('http://simpledesktops.com/',href),callback=self.get_url)
            


    def get_url(self,response):
        url= response.xpath('//div[@class="desktop"]/a/@href').extract()[0]
        yield scrapy.Request(urljoin('http://simpledesktops.com/',url),callback=self.get_img)

    def get_img(self,response):
        item=WallpaperItem()
        # item['src'] = response.xpath('//img/@src').extract()[0]
        item['src'] = response.url
        # print('\n',item['src'],'\n')
        yield item
        
