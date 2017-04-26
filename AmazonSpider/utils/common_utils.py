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
    product_list = get_yaml_info(product_path)
    return product_list


def get_product_code():
    """
    获取已有的商品编码列表
    :return: 商品编码列表
    """
    product_list = get_product_info()
    code_list = []
    for product in product_list:
        code_list.append(product['code'])
    return code_list


def get_urls_list():
    """
    生成横向爬虫的原始URL列表
    :return: URL列表
    """
    code_list = get_product_code()
    urls_list = []
    for code in code_list:
        url = 'https://www.amazon.co.jp/gp/product/', code
        urls_list.append(url)
    return urls_list


def slice_product_code(url):
    m = re.match(r'.*/(gp|dp|product)/(\w+)/.*$', url)
    if m:
        return m.group(2)
    else:
        raise Exception('未取到商品编码.')


if __name__ == '__main__':
    print get_product_code()