# -*- coding: utf-8 -*-
import scrapy


class UserspiderSpider(scrapy.Spider):
    name = 'UserSpider'
    allowed_domains = ['www.zhihu.com']
    start_urls = ['http://www.zhihu.com/']

    def parse(self, response):
        pass
