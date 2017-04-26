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
    # start_urls = common_utils.get_urls_list()
    start_urls = ['https://www.amazon.co.jp/gp/product/B000FP358E']
    code_list = common_utils.get_product_code()
    print code_list

    # rules = (
    #     Rule(LxmlLinkExtractor(allow=r'/dp/\w+/.*$')),
    #     Rule(LxmlLinkExtractor(allow=r'/.*/dp/\w+/.*$')),
    # )

    def parse(self, response):
        product_code = common_utils.slice_product_code(response.url)
        loader = ProductLoader(item=ProductDetail(), response=response)
        loader.add_value('productCode', product_code)
        loader.add_value('state', 1)
        center = loader.nested_xpath('//div[@id="centerCol"]')
        center.add_xpath('japaneseName', './/div[@id="title_feature_div"]//span/text()')
        center.add_xpath('seller', './/div[@id="title_feature_div"]//span/text()')
        center.add_value('extractTime', unicode(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
        yield loader.load_item()
