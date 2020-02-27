# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo


class QuotesspiderPipeline(object):
    def process_item(self, item, spider):
        return item


class mongodbPipeline(object):
    # 初始化mongodb参数
    def __init__(self, MONGO_URI, MONGO_DB):
        self.mongo_uri = MONGO_URI
        self.mongo_db = MONGO_DB

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            MONGO_URI=crawler.settings.get('MONGO_URI'),
            MONGO_DB=crawler.settings.get('MONGO_DB')
        )

    # 程序开始时连接MongoDB
    def open_spider(self,spider):
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]

    # 处理item
    def process_item(self, item, spider):
        self.db["Quotes"].insert(dict(item))
        return item

    # 关闭MongoDB
    def close_spider(self):
        self.client.close()
