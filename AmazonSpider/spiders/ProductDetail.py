# -*- coding: utf-8 -*-
import scrapy
import datetime

from scrapy.loader import ItemLoader
from scrapy.loader.processors import Compose
from AmazonSpider.items import ProductDetail


class ProductLoader(ItemLoader):
    default_output_processor = Compose(lambda v: v[0], unicode.strip)  # 移除头尾的空格


class ProductDetailSpider(scrapy.Spider):
    name = "ProductDetail"
    allowed_domains = ["amazon.co.jp"]
    start_urls = ['https://www.amazon.co.jp/gp/product/B000FP358E']

    def parse(self, response):
        loader = ProductLoader(item=ProductDetail(), response=response)
        center = loader.nested_xpath('//div[@id="centerCol"]')
        center.add_xpath('japanName', './/div[@id="title_feature_div"]//span/text()')
        center.add_xpath('product', './/div[@id="title_feature_div"]//span/text()')
        center.add_value('date', unicode(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
        return loader.load_item()
