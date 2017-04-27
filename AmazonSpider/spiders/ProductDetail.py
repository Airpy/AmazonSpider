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
    name = "ProductDetail"  # 爬虫的唯一标识
    allowed_domains = ["amazon.co.jp"]  # 仅允许在当前域名及子域名下爬虫
    # start_urls = common_utils.get_urls_list()
    start_urls = ['https://www.amazon.co.jp/gp/product/B000FP358E']
    code_list = common_utils.get_product_code()

    rules = (
        # 商品不同属性的链接URL
        Rule(LxmlLinkExtractor(allow=r'/dp/\w+/.*$',
                               restrict_xpaths='//div[@id="twister_feature_div"]//div[@id="variation_size_name"]//li',
                               tags=('a', 'area', 'li'),
                               attrs=('href', 'data-dp-url')),
             callback='parse_url'),
        # Frequently bought together区域商品
        Rule(LxmlLinkExtractor(allow=r'/.*/dp/\w+/.*$',
                               restrict_xpaths='//div[contains(@id, "sims-con")]//li[contains(@class, "a-align")]//a'),
             callback='parse_url'),
        # Customers Who Bought This Item Also Bought区域商品

    )

    def parse_start_url(self, response):
        product_code = unicode(common_utils.slice_product_code(response.url))
        loader = ProductLoader(item=ProductDetail(), response=response)
        loader.add_value('productCode', product_code)
        loader.add_value('state', unicode(1))
        center = loader.nested_xpath('//div[@id="centerCol"]')
        center.add_xpath('japaneseName', './/div[@id="title_feature_div"]//span/text()')
        center.add_xpath('seller', './/div[@id="title_feature_div"]//span/text()')
        center.add_value('extractTime', unicode(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
        yield loader.load_item()

    def parse_item(self, response):
        """
        解析
        :param response: 
        :return: 
        """
        pass
