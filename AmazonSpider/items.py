# -*- coding: utf-8 -*-
import scrapy


class ProductDetail(scrapy.Item):
    productCode = scrapy.Field()  # 商品编码
    state = scrapy.Field()  # 商品状态. 1: 正常; 0: 失效
    chineseName = scrapy.Field()  # 商品中文名称
    japanName = scrapy.Field()  # 商品日文名称
    imgUrl = scrapy.Field()  # 商品图片URL地址
    promotionFlag = scrapy.Field()  # 促销标识. 1: 当前享有促销; 0: 当前无促销
    seller = scrapy.Field()  # 卖家标识. 1: 自营; 2: 第三方货亚马逊销售; 3: 第三方
    minPrice = scrapy.Field()  # 历史最低价(不扣减积分)
    price = scrapy.Field()  # 商品价格
    pointFlag = scrapy.Field()  # 积分标识. 1: 当前享有积分; 0: 当前无积分
    points = scrapy.Field()  # 商品积分
    totalPrice = scrapy.Field()  # 商品最后价格(price-points)
    extractTime = scrapy.Field()  # 爬虫时间
