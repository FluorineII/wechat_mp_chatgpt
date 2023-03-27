from wechatpy import WeChatException


class CharGPTTimeOutException(WeChatException):
    """Invalid signature exception class"""

    def __init__(self, errcode=-50001, errmsg='chatgpt time out'):
        super(CharGPTTimeOutException, self).__init__(errcode, errmsg)
