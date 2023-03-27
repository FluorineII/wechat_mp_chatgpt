import os
import json
import base64
import time

import config
import wechat_mp_channel
from common.exception import CharGPTTimeOutException
from common.redisCache import RedisCache

global htmlResponse


# -*- coding:utf-8 -*-
def handler(event, context):
    global htmlResponse
    print('event is ', event)

    config.load_config()
    RedisCache.init(context)

    try:
        gptreq = wechat_mp_channel.get_and_reply(event)
        htmlResponse = {
            'statusCode': 200,
            'isBase64Encoded': True,
            'headers': {
                "Content-type": "text/html; charset=utf-8"
            },
            'body': base64.b64encode(str(gptreq).encode(encoding="utf-8")).decode(),
        }
    except CharGPTTimeOutException:
        # 等待五秒，接口自然超时
        print("chat gpt time out wait to retry")
        time.sleep(5)
        htmlResponse = {
            'statusCode': 403,
            'isBase64Encoded': True,
            'headers': {
                "Content-type": "text/html; charset=utf-8"
            },
            'body': "time out",
        }

    return json.dumps(htmlResponse)
