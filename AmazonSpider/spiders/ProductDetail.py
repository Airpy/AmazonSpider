# -*- coding: utf-8 -*-
import scrapy
import datetime

from scrapy.loader import ItemLoader
from scrapy.loader.processors import Compose
from AmazonSpider.items import ProductDetailItem
from AmazonSpider.items import ProductPriceItem


class ProductLoader(ItemLoader):
    default_output_processor = Compose(lambda v: v[0], unicode.strip)  # 移除头尾的空格


class ProductDetailSpider(scrapy.Spider):
    name = "ProductDetail"
    allowed_domains = ["amazon.co.jp"]
    start_urls = ['https://www.amazon.co.jp/gp/product/B000FP358E']

    def parse(self, response):
        loader1 = ProductLoader(item=ProductDetailItem(), response=response)
        loader2 = ProductLoader(item=ProductPriceItem(), response=response)
        center = loader1.nested_xpath('//div[@id="centerCol"]')
        center.add_xpath('japanName', './/div[@id="title_feature_div"]//span/text()')
        loader2.add_xpath('price', '//div[@id="centerCol"]//div[@id="title_feature_div"]//span/text()')
        # center.add_xpath('price', './/div[@id="title_feature_div"]//span/text()')
        # center.add_value('date', unicode(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
        return loader1.load_item(), loader2.load_item()
