import random
class RandomizedSet:

    def __init__(self):
        self.mp = {}
        
    def insert(self, val: int) -> bool:
        if val in self.mp:
            return False

        self.mp[val] = 1
        return True
        
    def remove(self, val: int) -> bool:
        if val in self.mp:
            del self.mp[val]
            return True

        return False

    def getRandom(self) -> int:
        # print(self.mp)
        k = random.randint(0, len(self.mp)-1)
        itr = 0
        for key, val in self.mp.items():
            if k == itr:
                return key
            itr += 1
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()