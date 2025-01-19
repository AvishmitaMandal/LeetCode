import heapq 

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        for x in range(len(nums)):
            nums[x] *= -1
            
        heapq.heapify(nums)

        while k>1:
            heapq.heappop(nums)
            k-= 1

        return -1 * heapq.heappop(nums)
        