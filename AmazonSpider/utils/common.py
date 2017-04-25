# -*- coding: utf-8 -*-
import datetime
import os
import logging
import sys
import re

from AmazonSpider.utils.yaml_utils import get_yaml_info


def get_now_time():
    """
    获取当前系统时间,如u'2017-04-25 21:59:06'
    :return: 当前系统时间
    """
    date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    return unicode(date)


def check_directory_exists(path):
    """
    判断指定目录是否存在
    :param path: 指定目录的绝对路径
    :return: 若存在则直接返回，否则创建该目录
    """
    if os.path.exists(path) and os.path.isdir(path):
        logging.info('目录[%s]已经存在' % path)
    else:
        os.makedirs(path)
        logging.warn('目录[%s]不存在，已经创建成功' % path)


def check_file_exists(path):
    """
    判断指定文件是否存在
    :param path: 指定文件
    :return: 若存在则直接返回，否则创建该文件
    """
    if os.path.exists(path) and os.path.isfile(path):
        logging.info('文件[%s]已经存在' % path)
    else:
        fp = open(path, 'w')
        fp.close()


def get_root_path():
    """
    获取项目根目录路径
    :return: 根目录路径
    """
    path_list = [path for path in sys.path if path.__contains__('AmazonSpider')]
    for aPath in path_list:
        if aPath.split(os.path.sep).count('AmazonSpider') != 1:
            continue
        else:
            return aPath


def get_product_info():
    """
    获取product.yaml文件商品信息
    :return: 商品信息
    """
    root_path = get_root_path()
    product_path = os.path.join(root_path, 'AmazonSpider/static/product/product.yaml')
    product = get_yaml_info(product_path)
    return product


def slice_product_code(url):
    m = re.match(r'.*/dp/(.*)/.*$', url)
    return m.group(1)

if __name__ == '__main__':
    print slice_product_code('/%E3%82%B9%E3%82%AD%E3%83%B3%E3%83%99%E3%83%BC%E3%83%97-%E8%99%AB%E3%82%88%E3%81%91%E3%82%B9%E3%83%97%E3%83%AC%E3%83%BC-%E3%83%9F%E3%82%B9%E3%83%88%E3%82%BF%E3%82%A4%E3%83%97-%E7%88%BD%E5%BF%AB%E3%82%B7%E3%83%88%E3%83%A9%E3%82%B9%E3%83%9E%E3%83%AA%E3%83%B3%E3%81%AE%E9%A6%99%E3%82%8A-%E7%B4%84666%E3%83%97%E3%83%83%E3%82%B7%E3%83%A5%E5%88%86/dp/B007G2WD28/ref=pd_sim_121_4?_encoding=UTF8&psc=1&refRID=8N0CW0TW86T920H10RVD')
