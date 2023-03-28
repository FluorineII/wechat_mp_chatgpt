import base64
import json

import config
import wechat_mp_channel
from common import cache
from common.exception import CharGPTTimeOutException
from common import log

global htmlResponse


# -*- coding:utf-8 -*-
def handler(event, context):
    global htmlResponse
    log.info('event is {}', event)
    config.load_config()
    cache.check_and_refresh()

    try:
        gptResp = wechat_mp_channel.get_and_reply(event)
        htmlResponse = {
            'statusCode': 200,
            'isBase64Encoded': True,
            'headers': {
                "Content-type": "text/html; charset=utf-8"
            },
            'body': base64.b64encode(str(gptResp).encode(encoding="utf-8")).decode(),
        }
    except CharGPTTimeOutException:
        # 等待五秒，函数继续处理，接口自然超时
        log.info("chat gpt time out wait to retry")
        #time.sleep(5)
        htmlResponse = {
            'statusCode': 403,
            'isBase64Encoded': True,
            'headers': {
                "Content-type": "text/html; charset=utf-8"
            },
            'body': "time out",
        }

    return json.dumps(htmlResponse)
