# -*- coding: utf-8 -*-
import datetime

from scrapy.linkextractors.lxmlhtml import LxmlLinkExtractor
from scrapy.loader import ItemLoader
from scrapy.loader.processors import Compose
from scrapy.spiders import CrawlSpider, Rule
from AmazonSpider.items import ProductDetail
from AmazonSpider.utils import common_utils


class ProductLoader(ItemLoader):
    default_output_processor = Compose(lambda v: v[0], unicode.strip)  # 移除头尾的空格


class ProductDetailSpider(CrawlSpider):
    name = "ProductDetail"
    allowed_domains = ["amazon.co.jp"]
    start_urls = ['https://www.amazon.co.jp/gp/product/B000FP358E']
    products = common_utils.get_product_info()
    rules = (
        Rule(LxmlLinkExtractor(allow=r''))
    )

    def parse(self, response):
        loader = ProductLoader(item=ProductDetail(), response=response)
        # loader.add_value('productCode', self.start_code)
        loader.add_value('state', 1)
        center = loader.nested_xpath('//div[@id="centerCol"]')
        center.add_xpath('japanName', './/div[@id="title_feature_div"]//span/text()')
        center.add_xpath('product', './/div[@id="title_feature_div"]//span/text()')
        center.add_value('date', unicode(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
        return loader.load_item()
