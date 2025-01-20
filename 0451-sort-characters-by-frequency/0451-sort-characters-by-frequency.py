from collections import defaultdict
import heapq

class Solution:
    def frequencySort(self, s: str) -> str:
        frequency = defaultdict(int)
        
        for c in s:
            frequency[c] += 1

        heap = []
        for key, val in frequency.items():
            heapq.heappush(heap, (-1*val, key))

        res = ''
        while heap:
            val, key = heapq.heappop(heap)
            val *= -1
            for x in range(val):
                res += key

        return res
        