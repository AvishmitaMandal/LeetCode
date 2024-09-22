class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        self.str = characters
        self.length = combinationLength
        self.list = []

    def mapping(self):
        res = ""
        for x in range(len(self.list)):
            if self.list[x] == 1:
                res += self.str[x]

        return res
        

    def next(self) -> str:
        if len(self.list) == 0:
            for x in range(self.length):
                self.list.append(1)
            for x in range(len(self.str)-self.length):
                self.list.append(0)
            print(self.list)
            res = self.mapping()
            return res

            
        if self.hasNext():
            # last element is 1
            if self.list[len(self.list)-1] == 1:
                x, count = len(self.list) - 1, 0
                while self.list[x] == 1:
                    count += 1
                    self.list[x] = 0
                    x -= 1

                for y in range(x, -1, -1):
                    if self.list[y] == 1:
                        self.list[y] = 0
                        self.list[y+1] = 1
                        for x in range(count):
                            self.list[y+2+x] = 1
                        break
                print(self.list)    

            else:
                for x in range(len(self.list)-1, -1, -1):
                    if self.list[x] == 1:
                        self.list[x] = 0
                        self.list[x+1] = 1
                        break
                print(self.list)

            res = self.mapping()
        
            return res

    def hasNext(self) -> bool:
        if len(self.list) == 0:
            print(self.list)
            return True
        count, x = 0, len(self.list)-1
        while True:
            if self.list[x] == 1:
                count += 1
                if count == self.length:
                    return False
            else:
                break
            x -= 1

        return True

        


# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()