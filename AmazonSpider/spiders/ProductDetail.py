# -*- coding: utf-8 -*-
import scrapy
import datetime
from scrapy.loader import ItemLoader
from AmazonSpider.items import ProductDetailItem


class ProductDetailSpider(scrapy.Spider):
    name = "ProductDetail"
    allowed_domains = ["amazon.co.jp"]
    start_urls = ['https://www.amazon.co.jp/gp/product/B000FP358E']

    def parse(self, response):
        loader = ItemLoader(item=ProductDetailItem(), response=response)
        center = loader.nested_xpath('//div[@id="centerCol"]')
        center.add_xpath('name', './/div[@id="title_feature_div"]//span/text()')
        center.add_xpath('price', './/div[@id="title_feature_div"]//span/text()')
        center.add_value('date', datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        loader.load_item()
