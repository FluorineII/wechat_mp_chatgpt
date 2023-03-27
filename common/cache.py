import json
import os

#config_path = "code/localStorage.json"
config_path = "localStorage.json"


def get(key):
    cache = get_cache()
    return cache.get(key)


def get_cache():
    if not os.path.exists(config_path):
        raise Exception('配置文件不存在')

    cache_str = read_file(config_path)
    # 将json字符串反序列化为dict类型
    cache = json.loads(cache_str)
    return cache


def set_key(key, value):
    cache = get_cache()
    cache[key] = value
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
    with open(config_path, 'w') as file:
        # Write the modified contents to the file
        file.write(json.dumps(cache))