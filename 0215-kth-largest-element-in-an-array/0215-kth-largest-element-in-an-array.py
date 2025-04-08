import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        '''
        Input: nums = [3,2,1,5,6,4], k = 2
        Output: 5

        [6,5,4,3,2,1]

        Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
        Output: 4
        
        min-heap
        -6
        -5
        -5
        -4
        -3
        -3
        -2
        -2
        -1

        
        '''
        hp = []
        for num in nums:
            heapq.heappush(hp, num)
            if len(hp) > k:
                heapq.heappop(hp)

        return hp[0]
            