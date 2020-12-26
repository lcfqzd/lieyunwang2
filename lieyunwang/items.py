# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class LieyunwangItem(scrapy.Item):
    # define the fields for your item here like:
    imgsrc = scrapy.Field()
    imgalt = scrapy.Field()
    time = scrapy.Field()
