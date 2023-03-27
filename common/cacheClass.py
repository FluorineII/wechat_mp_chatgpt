class CacheClass(object):
    @staticmethod
    def init(context):
        raise NotImplementedError

    def get(self, key):
        raise NotImplementedError

    def get_cache(self):
        raise NotImplementedError

    def set_key(self, key, value):
        raise NotImplementedError

    def pop(self, key):
        raise NotImplementedError
