import json
import os
import time

from common.log import logger

# config_path = "code/localStorage.json"
cache_path = "/tmp/localStorage.json"


def get(key):
    cache = get_cache()
    return cache.get(key)


def get_cache():
    if not os.path.exists(cache_path):
        logger.info('配置文件不存在，创建新文件')
        save_file({"timestamp"})
        return {}

    cache_str = read_file(cache_path)
    # 将json字符串反序列化为dict类型
    cache = json.loads(cache_str)
    return cache


def set_key(key, value):
    cache = get_cache()
    cache[key] = value
    save_file(cache)


def del_key(key):
    cache = get_cache()
    del cache[key]
    save_file(cache)


def pop(key):
    cache = get_cache()
    cache.pop(key)
    save_file(cache)


def read_file(path):
    with open(path, mode='r', encoding='utf-8') as f:
        return f.read()


def save_file(cache):
    # Open the file in write mode
    with open(cache_path, 'w') as file:
        # Write the modified contents to the file
        file.write(json.dumps(cache))


def new_cache():
    timestamp = time.time()
    return {"time": timestamp}


def check_and_refresh():
    preTime = get("time")
    if not preTime:
        preTime = 0
    if time.time() - preTime > 3600:
        save_file(new_cache())
