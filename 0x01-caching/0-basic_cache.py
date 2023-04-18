#!/usr/bin/python3
""" BasicCache module"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """ BasicCache defines:
      - caching system with a dictionary
    """
    def put(self, key, item):
        """ Add an item in the cache"""
        if key is None or item is None:
            pass
        else:
            self.cache_data[key] = item

    def get(self, key):
        """ Get an item by the respective key"""
        if key is None or key not in self.cache_data:
            return None
        else:
            return self.cache_data[key]
