class OrderedStream:

    def __init__(self, n: int):
        self.n = n
        self.ptr = 0
        self.list = []
        for x in range(self.n):
            self.list.append("*")

    def insert(self, idKey: int, value: str) -> List[str]:
        self.list[idKey-1] = value
        res = []
        if self.list[self.ptr] != "*":
            while self.ptr < self.n and self.list[self.ptr] != "*":
                res.append(self.list[self.ptr])
                self.ptr += 1

        return res

        
        


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)