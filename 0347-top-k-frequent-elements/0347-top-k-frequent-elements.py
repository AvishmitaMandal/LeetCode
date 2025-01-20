import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}

        for num in nums:
            if num not in hashmap:
                hashmap[num] = 1
            else:
                hashmap[num] += 1
        
        hq = []
        heapq.heapify(hq)

        for key, value in hashmap.items():
            heapq.heappush(hq, (-1*value, key))

        res = []

        while k:
            (val, key) = heapq.heappop(hq)
            res.append(key)
            k-= 1

        return res
        