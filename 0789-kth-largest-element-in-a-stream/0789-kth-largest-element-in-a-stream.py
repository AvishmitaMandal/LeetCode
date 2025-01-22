import heapq
class KthLargest:
    '''
         [4, 5, 8, 2] -> [2, 4, 5, 5, 8, 9, 10]
    '''

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums
        self.n = len(nums)
        heapq.heapify(self.nums)

        if self.n > self.k:
            while self.n != self.k:
                heapq.heappop(self.nums)
                self.n -= 1
        

    def add(self, val: int) -> int:
        if self.n < self.k:
            heapq.heappush(self.nums, val)
            self.n += 1

        else :
            heapq.heappush(self.nums, val)
            heapq.heappop(self.nums)
            
        res = heapq.heappop(self.nums)
        heapq.heappush(self.nums, res)
        return res
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)