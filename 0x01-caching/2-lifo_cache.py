#!/usr/bin/env python3
""" lifo_cache """


BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """ lifo_cache class """
    last = None

    def __init__(self):
        """ constructor """
        super().__init__()

    def put(self, key, item):
        """ put method to take data using FIFO method """
        if key and item:
            if key in self.cache_data.keys():
                self.cache_data[key] = item
                self.last = key
                return
            if len(self.cache_data) == BaseCaching.MAX_ITEMS:
                self.cache_data.pop(self.last)
                print('DISCARD:', self.last)
            self.cache_data[key] = item
            self.last = key

    def get(self, key):
        """ get method to get data """
        if key and key in self.cache_data.keys():
            return self.cache_data[key]
        else:
            return None
