from collections import OrderedDict

class LRUCache:

    def __init__(self, capacity: int):
        self.dict = OrderedDict()
        self.capacity = capacity
        

    def get(self, key: int) -> int:
        if key in self.dict:
            val = self.dict.pop(key)
            self.dict[key] = val
            return val
        
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.dict:
            val = self.dict.pop(key)
            self.dict[key] = value

        elif len(self.dict) == self.capacity:
            # remove the first item
            self.dict.popitem(last = False)
            # and then insert key-value
            self.dict[key] = value

        else:
            # insert the key-value
            self.dict[key] = value
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)