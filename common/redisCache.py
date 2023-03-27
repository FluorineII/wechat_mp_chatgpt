import json

from common.cacheClass import CacheClass
import redis

global client


class RedisCache(CacheClass):

    @staticmethod
    def init(context):
        global client
        logger = context.getLogger()
        redis_port = context.getUserData("redis_port")  # from function env get redis port
        redis_host = context.getUserData("redis_host")  # from function env get redis host
        redis_password = context.getUserData("redis_password")  # from function env get redis password
        logger.info("===========redis host={}".format(redis_host))
        logger.info("===========redis port={}".format(redis_port))
        client = redis.StrictRedis(host=redis_host, port=redis_port, password=redis_password)

    def get(self, key):
        cacheStr = json.loads(client.get(key))
        print("key:{}, value:{}", key, cacheStr)

    def get_cache(self):
        pass

    def set_key(self, key, value):
        cacheStr = json.dumps(value)
        client.set(key, cacheStr, ex=300)

    def pop(self, key):
        client.delete(key)
