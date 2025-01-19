# unpacking iterables in python

import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        euc_dist = []
        heapq.heapify(euc_dist)

        for point in points:
            x, y = point[0], point[1]
            ed = x*x + y*y
            heapq.heappush(euc_dist, (ed, point))
        
        res = []
        while k:
            (ed, point) = heapq.heappop(euc_dist)
            res.append(point)
            k-=1

        return res


        