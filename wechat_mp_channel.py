import base64
import time
from concurrent.futures import ThreadPoolExecutor

from wechatpy import parse_message, create_reply
from wechatpy.exceptions import InvalidSignatureException, InvalidAppIdException
from wechatpy.utils import check_signature

from chatgpt.chatgpt_model import ChatGPTModel
from common import cache
from common.exception import CharGPTTimeOutException
from common import log
from config import conf

thread_pool = ThreadPoolExecutor(max_workers=8)


def get_and_reply(request):
    config = conf()
    signParam = request.get("queryStringParameters", "")
    signature = signParam.get("signature", "")
    timestamp = signParam.get("timestamp", "")
    nonce = signParam.get("nonce", "")
    encrypt_type = signParam.get("encrypt_type", "raw")
    msg_signature = signParam.get("msg_signature", "")
    try:
        check_signature(config["token"], signature, timestamp, nonce)
    except InvalidSignatureException:
        return ""
    if request["httpMethod"] == "GET":
        echo_str = signParam["echostr"]
        return echo_str
    # POST request
    if encrypt_type == "raw":
        # plaintext mode
        msg = base64.b64decode(request["body"]).decode("utf-8")
        msg = parse_message(msg)
        if msg.type == "text":
            retMsg = reply_with_gpt(msg)
            log.info("msg from gpt is {}", retMsg)
            reply = create_reply(retMsg, msg)
        else:
            reply = create_reply("Sorry, can not handle this for now", msg)
        return reply.render()
    else:
        # encryption mode
        from wechatpy.crypto import WeChatCrypto

        crypto = WeChatCrypto(config["token"], config["encoding_aes_key"], config["app_id"])
        try:
            msg = base64.b64decode(request["body"]).decode("utf-8")
            msg = crypto.decrypt_message(msg, msg_signature, timestamp, nonce)
        except (InvalidSignatureException, InvalidAppIdException):
            return ""
        else:
            msg = parse_message(msg)
            if msg.type == "text":
                retMsg = reply_with_gpt(msg)
                log.info("msg from gpt is {}", retMsg)
                reply = create_reply(retMsg, msg)
            else:
                reply = create_reply("Sorry, can not handle this for now", msg)
            return crypto.encrypt_message(reply.render(), nonce, timestamp)


def reply_with_gpt(msg):
    log.info('[WX_Public] receive public msg: {}, userId: {}'.format(msg.content, msg.source))
    key = msg.content + '|' + msg.source
    gptCache = cache.get(key)
    log.info("cache before gpt is {}", gptCache)
    if gptCache:
        # request time
        gptCache['req_times'] += 1
        cache.set_key(key, gptCache)
    return WechatSubscribeAccount().handle(msg)


class WechatSubscribeAccount(object):
    def handle(self, msg, count=1):
        if msg.content == "继续":
            return self.get_un_send_content(msg.source)

        context = dict()
        context['from_user_id'] = msg.source
        key = msg.content + '|' + msg.source
        res = cache.get(key)
        if not res:
            # cache[key] = {"status": "waiting", "req_times": 1}
            cache.set_key(key, {"status": "waiting", "req_times": 1})
            thread_pool.submit(self._do_send, msg.content, context)

        res = cache.get(key)
        if res.get('status') == 'success':
            res['status'] = "done"
            cache.pop(key)
            return res.get("data")

        if cache.get(key)['req_times'] >= 2 and count >= 4:
            return "已开始处理，请稍等片刻后输入\"继续\"查看回复"

        if count <= 5:
            time.sleep(1)
            if count == 5:
                # 第5秒不做返回，防止消息发送出去了但是微信已经中断连接
                raise CharGPTTimeOutException()
            return self.handle(msg, count + 1)

    def _do_send(self, query, context):
        key = query + '|' + context['from_user_id']
        reply_text = ChatGPTModel().reply(query, context)
        log.info('[WX_Public] reply content: {}'.format(reply_text))
        newCache = cache.get(key)
        newCache['status'] = "success"
        newCache['data'] = reply_text
        # cache[key] = newCache
        cache.set_key(key, newCache)
        log.info("cache after gpt is {}", cache.get_cache())

    def get_un_send_content(self, from_user_id):
        contentCache = cache.get_cache()
        for key in contentCache:
            # key 是 content｜user_id 的格式
            if '|'+from_user_id in key:
                value = contentCache[key]
                if value.get('status') == "success":
                    cache.pop(key)
                    return value.get("data")
                return "还在处理中，请稍后再试"
        return "目前无等待回复信息，请输入对话"
