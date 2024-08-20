#!/usr/bin/env python3
""" fifo_cache """


BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """ fifo_cache class """
    def __init__(self):
        """ constructor """
        super().__init__()

    def put(self, key, item):
        """ put method to take data using FIFO method """
        if key and item:
            self.cache_data[key] = item
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                first_item = next(iter(self.cache_data))
                self.cache_data.pop(first_item)
                print('DISCARD:', first_item)

    def get(self, key):
        """ get method to get data """
        if key and key in self.cache_data.keys():
            return self.cache_data[key]
        else:
            return None
