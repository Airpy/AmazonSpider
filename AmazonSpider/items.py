# -*- coding: utf-8 -*-
import scrapy


class ProductDetailItem(scrapy.Item):
    name = scrapy.Field()  # 商品名称
    # img = scrapy.Field()  # 商品图片地址
    price = scrapy.Field()  # 商品价格
    # points = scrapy.Field()  # 亚马逊积分
    # promotion = scrapy.Field(serialezer=bool)  # 1: 当前享有促销; 0: 当前无促销
    # seller = scrapy.Field(serializer=int)  # 1: 自营; 2: 第三方货亚马逊销售; 3: 第三方
    date = scrapy.Field(serializer=str)  # 爬虫时间
