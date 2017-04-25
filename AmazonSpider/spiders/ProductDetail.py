# -*- coding: utf-8 -*-
import scrapy
import datetime

from scrapy.loader import ItemLoader
from scrapy.loader.processors import Compose
from AmazonSpider.items import ProductPriceItem
from AmazonSpider.items import Product


class ProductLoader(ItemLoader):
    default_output_processor = Compose(lambda v: v[0], unicode.strip)  # 移除头尾的空格


class ProductDetailSpider(scrapy.Spider):
    name = "ProductDetail"
    allowed_domains = ["amazon.co.jp"]
    start_urls = ['https://www.amazon.co.jp/gp/product/B000FP358E']

    def parse(self, response):
        loader = ProductLoader(item=Product(), response=response)
        center = loader.nested_xpath('//div[@id="centerCol"]')
        center.add_xpath('japanName', './/div[@id="title_feature_div"]//span/text()')
        center.add_xpath('product', './/div[@id="title_feature_div"]//span/text()')
        center.add_value('date', unicode(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
        return loader.load_item()
        # item1 = Product()
        # item2 = ProductDetailItem()
        # item2['product'] = item1
        # item1['japanName'] = response.xpath('//div[@id="centerCol"]//div[@id="title_feature_div"]//span/text()').extract_first().strip()
        # item2['pointFlag'] = response.xpath('//div[@id="centerCol"]//div[@id="title_feature_div"]//span/text()').extract_first().strip()
        # return item2