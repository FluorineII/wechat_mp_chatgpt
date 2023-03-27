# encoding:utf-8

import json
import os

config = {}


def load_config():
    global config
    config = {
        "api_key": "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",
        "model": "gpt-3.5-turbo",
        "conversation_max_tokens": 1000,
        "character_desc": "你是ChatGPT, 一个由OpenAI训练的大型语言模型, 你旨在回答并解决人们的任何问题，并且可以使用多种语言与人交流。",
        "token": "huqi",
        "key": "yZnPNRSU3ZDKrynJc8tZu5E9ejkibferuC9JXpYVXMQ",
        "app_id": "wx7876c808fadac136"
    }

    print("Load config success")
    return config


def get_root():
    return os.path.dirname(os.path.abspath(__file__))


def conf():
    return config
