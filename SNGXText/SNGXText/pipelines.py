# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class SngxtextPipeline(object):
    def open_spider(self, spider):
        # self.filename = open('shaoniangexing.txt', 'w', encoding='utf-8')
        # self.filename = open('shaoniangexing2.txt', 'w', encoding='utf-8')
        # self.filename = open('shaoniangexing3.txt', 'w', encoding='utf-8')
        self.filename = open('shaoniangexing4.txt', 'w', encoding='utf-8')

    def process_item(self, item, spider):
        info = item['title'] + '\n' + item['content'] + '\n'
        self.filename.write(info)
        self.filename.flush()
        return item

    def close_spider(self, spider):
        self.filename.close()
