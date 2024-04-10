#!/usr/bin/env python3
"""LFU caching
"""

BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    """LFU cache
    """

    def __init__(self):
        """Constructor
        """
        super().__init__()
        self.lfu_keys = {}

    def put(self, key, item):
        """Add an item in the cache
        """
        if key and item and self.cache_data.get(key) != item:

            self.cache_data[key] = item
            if len(self.cache_data) > self.MAX_ITEMS:
                k = min(self.lfu_keys, key=self.lfu_keys.get)
                self.cache_data.pop(k)
                self.lfu_keys.pop(k)
                print(f"DISCARD: {k}")

            self.lfu_keys[key] = self.lfu_keys.get(key, 0) + 1

    def get(self, key):
        """ Get an item by key """
        if key in self.lfu_keys:
            self.lfu_keys[key] += 1
        return self.cache_data.get(key)


# my_cache = LFUCache()
# my_cache.put("A", "Hello")
# my_cache.put("B", "World")
# my_cache.put("C", "Holberton")
# my_cache.put("D", "School")
# my_cache.print_cache()
# print(my_cache.get("B"))
# my_cache.put("E", "Battery")
# my_cache.print_cache()
# my_cache.put("C", "Street")
# my_cache.print_cache()
# print(my_cache.get("A"))
# print(my_cache.get("B"))
# print(my_cache.get("C"))
# my_cache.put("F", "Mission")
# my_cache.print_cache()
# my_cache.put("G", "San Francisco")
# my_cache.print_cache()
# my_cache.put("H", "H")
# my_cache.print_cache()
# my_cache.put("I", "I")
# my_cache.print_cache()
# print(my_cache.get("I"))
# print(my_cache.get("H"))
# print(my_cache.get("I"))
# print(my_cache.get("H"))
# print(my_cache.get("I"))
# print(my_cache.get("H"))
# my_cache.put("J", "J")
# my_cache.print_cache()
# my_cache.put("K", "K")
# my_cache.print_cache()
# my_cache.put("L", "L")
# my_cache.print_cache()
# my_cache.put("M", "M")
# my_cache.print_cache()
