class RecentCounter:

    def __init__(self):
        self.list = []
        
    def ping(self, t: int) -> int:
        self.list.append(t)

        if len(self.list) == 1:
            self.start = 0
            self.end = 0
        else:
            self.end += 1
            while True:
                if self.list[self.end] - self.list[self.start]<=3000:
                    break
                self.start += 1

        return self.end - self.start + 1
        
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)