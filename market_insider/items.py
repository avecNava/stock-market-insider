# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MarketInsiderItem(scrapy.Item):

    ticker = scrapy.Field()
    name = scrapy.Field()
    price = scrapy.Field()
    pct = scrapy.Field()
    datetime=scrapy.Field()
