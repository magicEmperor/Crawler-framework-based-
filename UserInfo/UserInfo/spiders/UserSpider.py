# -*- coding: utf-8 -*-
import scrapy


class UserspiderSpider(scrapy.Spider):
    name = 'UserSpider'
    allowed_domains = ['www.zhihu.com']
    start_urls = ['http://www.zhihu.com/']
    def start_requests(self):
        # url = 'https://www.zhihu.com/people/lengyue233'
        url = 'https://www.zhihu.com/api/v4/members/Germey/followees?include=data%5B*%5D.answer_count%2Carticles_count%2Cgender%2Cf'
        yield scrapy.Request(url=url,callback=self.parse)
    def parse(self, response):
        print(response.text)
