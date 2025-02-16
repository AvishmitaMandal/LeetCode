import random

class RandomizedSet:

    def __init__(self):
        self.mp = {}
        self.array_list = []
        self.count = 0

    def insert(self, val: int) -> bool:
        if val in self.mp:
            return False

        self.array_list.append(val)
        self.count += 1
        self.mp[val] = self.count - 1
        return True
        
    def remove(self, val: int) -> bool:
        if val not in self.mp:
            return False

        del_ele_index = self.mp[val]
        last_ele_index = self.count - 1

        del_ele = self.array_list[del_ele_index]
        last_ele = self.array_list[last_ele_index]
        
        # make changes in map
        self.mp[last_ele] = del_ele_index
        del self.mp[del_ele]

        # make changes in list
        self.array_list[del_ele_index] = last_ele
        self.array_list.pop()

        self.count -= 1
        # print("Remove : ", val)
        # print(self.array_list)
        # print(self.mp)
        return True
        

    def getRandom(self) -> int:
        k = random.randint(0,self.count-1)
        return self.array_list[k]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()