#!/usr/bin/env python3
""" LRU_cache """
from collections import OrderedDict


BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """ LRUCache class """

    def __init__(self):
        """ constructor """
        super().__init__()
        self.cache_data = OrderedDict(self.cache_data)

    def put(self, key, item):
        """ put method to take data using LRU method """
        if key and item:
            if key in self.cache_data.keys():
                self.cache_data[key] = item
                self.cache_data.move_to_end(key)
                return
            if len(self.cache_data) == BaseCaching.MAX_ITEMS:
                poped = self.cache_data.popitem(last=False)
                print('DISCARD:', poped[0])
                self.cache_data[key] = item
                return
            self.cache_data[key] = item

    def get(self, key):
        """ get method to get data """
        if key and key in self.cache_data.keys():
            self.cache_data.move_to_end(key)
            return self.cache_data[key]
        else:
            return None
