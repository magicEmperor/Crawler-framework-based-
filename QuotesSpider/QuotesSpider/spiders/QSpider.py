# -*- coding: utf-8 -*-
import scrapy


class QspiderSpider(scrapy.Spider):
    name = 'QSpider'
    allowed_domains = ['http://quotes.toscrape.com/']
    start_urls = ['http://http://quotes.toscrape.com//']

    def parse(self, response):
        pass
