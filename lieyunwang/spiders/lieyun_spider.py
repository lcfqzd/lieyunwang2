# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

class LieyunSpiderSpider(CrawlSpider):
    name = 'lieyun_spider'
    allowed_domains = ['lieyunwang.com']
    start_urls = ['https://www.lieyunwang.com/latest/p1.html']

    rules = (
        # https://www.lieyunwang.com/latest/p1.html
        Rule(LinkExtractor(allow=r'latest/p\d+\.html'), follow=True),
        Rule(LinkExtractor(allow=r'/archives/\d+'), callback='parse_item', follow=False)
    )



    def parse_item(self, response):
        # imgsrc: //div[@class="shade pore mb30"]/img[@class="img-fuil img-round"]/@src
        # imgalt: //div[@class="shade pore mb30"]/img[@class="img-fuil img-round"]/@alt
        # time: //div[@id="main-text-id"]/p[1]/strong/text()

        item = {}

        item['imgsrc'] = response.xpath('//div[@class="shade pore mb30"]/img[@class="img-fuil img-round"]/@src').get()
        item['imgalt'] = response.xpath('//div[@class="shade pore mb30"]/img[@class="img-fuil img-round"]/@alt').get()
        item['time'] = response.xpath('//div[@id="main-text-id"]/p[1]/strong/text()').get()


        # print(item)

        return item
