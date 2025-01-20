from collections import defaultdict
import heapq

class Solution:
    def frequencySort(self, s: str) -> str:
        frequency = defaultdict(int)
        
        for c in s:
            frequency[c] += 1

        heap = []
        for key, val in frequency.items():
            heapq.heappush(heap, (-val, key))

        res = []
        while heap:
            val, key = heapq.heappop(heap)
            res.append(key*-val)

        return ''.join(res)
        