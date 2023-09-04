https://leetcode.com/problems/lru-cache/description/

from collections import OrderedDict
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key: int) -> int:
        value = self.cache.pop(key, None)
        if value is None:
            return -1
        self.cache[key] = value
        return value
		
	# or use move_to_end
	def get(self, key: int) -> int:
        res = self.cache.get(key, -1)
        if res != -1:
            self.cache.move_to_end(key)
        return res

    def put(self, key: int, value: int) -> None:
        if not self.cache.pop(key, None) and self.capacity == len(self.cache):
            self.cache.popitem(last=False)
        self.cache[key] = value


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)