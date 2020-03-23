# -*- coding: utf-8 -*-
import re
import scrapy


class QikuaiSpider(scrapy.Spider):
    name = 'qikuai'
    allowed_domains = ['7kzw.com']
    url = 'https://www.7kzw.com'
    # start_urls = [url + '/52/52971/13174830.html']
    # start_urls = [url + '/52/52971/13174916.html']
    # start_urls = [url + '/52/52971/43357434.html']
    start_urls = [url + '/52/52971/43357505.html']

    def parse(self, response):
        title = response.xpath('//h1/text()').extract()[0]
        content = response.xpath('string(//div[@id="content"])').extract()[0].strip().replace('\xa0\xa0\xa0\xa0', '\n')
        content = content.replace("天才一秒记住本站地址：[奇快中文网]\r\n\t\t\t\thttps://www.7kzw.com/最快更新！无广告！\r\n\t\t\t\r\n\t\t\t", "")
        content = content.replace("\t\t\t\r\n\t\t\t\r\n\t\t\t\t章节错误,点此报送(免注册),\r\n\t\t\t\t报送后维护人员会在两分钟内校正章节内容,请耐心等待。", "")
        next_url = response.xpath('//a[@class="next"]/@href').extract_first()

        yield {
            'title': title,
            'content': content
        }
        yield scrapy.Request(response.urljoin(next_url), callback=self.parse)
