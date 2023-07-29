#LRU Cache (Least recently used)
from collections import OrderedDict
class LRU:
    def __init__(self,capacity):
        self.cache  = OrderedDict()
        self.capacity = capacity
    
    def get(self,key):
        if key not in self.cache:
            return -1
        self.cache.move_to_end(key)
        return self.cache[key]
    
    def put(self,key,value):
        self.cache[key] = value
        self.cache.move_to_end(key)
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)

cache = LRU(2)
cache.put(1, 1)
print(cache.cache)
cache.put(2, 2)
print(cache.cache)
cache.get(1)
print(cache.cache)
cache.put(3, 3)
print(cache.cache)
cache.get(2)
print(cache.cache)
cache.put(4, 4)
print(cache.cache)
cache.get(1)
print(cache.cache)
cache.get(3)
print(cache.cache)
cache.get(4)
print(cache.cache)
        
