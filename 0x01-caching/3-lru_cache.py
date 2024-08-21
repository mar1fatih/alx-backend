#!/usr/bin/env python3
""" lifo_cache """


BaseCaching = __import__('base_caching').BaseCaching


def old_num(LRU):
    """ find the min """
    min = None
    for k in LRU.keys():
        if min is None:
            min = LRU[k]
        if LRU[k] < min:
            min = LRU[k]
    return min


class LRUCache(BaseCaching):
    """ LRUCache class """
    count = 0
    old = 1
    LRU = dict()

    def __init__(self):
        """ constructor """
        super().__init__()

    def put(self, key, item):
        """ put method to take data using LRU method """
        if key and item:
            if key in self.cache_data.keys():
                self.cache_data[key] = item
                self.count += 1
                self.LRU[key] = self.count
                self.old = old_num(self.LRU)
                return
            if len(self.cache_data) == BaseCaching.MAX_ITEMS:
                for k in self.LRU.keys():
                    if self.LRU[k] == self.old:
                        print('DISCARD:', k)
                        self.cache_data.pop(k)
                        self.LRU.pop(k)
                        self.old = old_num(self.LRU)
                        break
                self.cache_data[key] = item
                self.count += 1
                self.LRU[key] = self.count
                return
            self.cache_data[key] = item
            self.count += 1
            self.LRU[key] = self.count

    def get(self, key):
        """ get method to get data """
        if key and key in self.cache_data.keys():
            self.count += 1
            self.LRU[key] = self.count
            return self.cache_data[key]
        else:
            return None
