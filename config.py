# encoding:utf-8

import json
import os

from common.log import logger

config = {}
# config_path = "code/config.json"  # 华为functionGraph的文件在code目录下
config_path = "config.json"


def load_config():
    global config
    config = get_config()
    logger.info("Load config success")
    return config


def get_config():
    if not os.path.exists(config_path):
        raise Exception('配置文件不存在')

    cache_str = read_file(config_path)
    # 将json字符串反序列化为dict类型
    cache = json.loads(cache_str)
    return cache


def read_file(path):
    with open(path, mode='r', encoding='utf-8') as f:
        return f.read()


def conf():
    return config
