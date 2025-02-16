import random
class RandomizedCollection:

    def __init__(self):
        self.mp = {}
        self.array_list = []
        self.count = 0
        
    def insert(self, val: int) -> bool:
        self.count += 1
        self.array_list.append(val)

        if val not in self.mp or not self.mp[val]:
            self.mp[val] = {}
            self.mp[val][self.count-1] = 1
            # print("insert: ", val)
            # print(self.array_list)
            # print(self.mp)
            return True

        self.mp[val][self.count-1] = 1
        # print("insert: ", val)
        # print(self.array_list)
        # print(self.mp)
        return False
            
    def remove(self, val: int) -> bool:
        if val not in self.mp or not self.mp[val]:
            # print("remove: ", val)
            # print(self.array_list)
            # print(self.mp)
            return False

        del_index = next(iter(self.mp[val]))
        del_ele = self.array_list[del_index]

        last_index = len(self.array_list)-1
        last_ele = self.array_list[last_index]

        # swap in list
        self.array_list[del_index] = last_ele
        self.array_list.pop()

        # change in map
        if self.count == 1:
            self.array_list = []
            self.mp = {}

        elif del_ele == last_ele and del_index != last_index:
            del self.mp[last_ele][last_index]

        else:
            del self.mp[last_ele][last_index]
            self.mp[last_ele][del_index] = 1
            del self.mp[del_ele][del_index]

        self.count -= 1
        # print("remove: ", val)
        # print(self.array_list)
        # print(self.mp)
        return True

    def getRandom(self) -> int:
        k = random.randint(0, self.count - 1)
        return self.array_list[k]


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()