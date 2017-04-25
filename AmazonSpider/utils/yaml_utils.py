# -*- coding: utf-8 -*-
import logging
import yaml


def get_yaml_info(yaml_file):
    """
    读取YAML文件并返回文件内容（字典）
    :param yaml_file: 需要被解析的YAML文件（绝对路径）
    :return: 解析后的字典
    """
    with open(yaml_file, 'r') as stream:
        try:
            return yaml.load(stream)
        except yaml.YAMLError as exc:
            logging.error('加载[%s]文件失败,原因为:[%s]' % (yaml_file, exc))


def dump_yaml_info(yaml_file, data):
    """
    将指定内容写入YAML文件
    :param yaml_file: 需要被写入的文件（绝对路径）
    :param data: 需要被写入的内容
    """
    with open(yaml_file, 'w') as stream:
        try:
            yaml.dump(data, stream)
        except yaml.YAMLError as exc:
            logging.error('写入YAML文件失败，指定的文件为[%s]，指定的数据为[%s],原因为:[%s]' % (yaml_file, data, exc))
