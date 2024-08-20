#!/usr/bin/env python3
"""0-basic_cache.py"""


BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """ basic_cache class """
    def __init__(self):
        """constructor"""
        super().__init__()

    def put(self, key, item):
        """ put method to take data """
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """ get method to get data """
        if key and key in self.cache_data.keys():
            return self.cache_data[key]
        else:
            return None
