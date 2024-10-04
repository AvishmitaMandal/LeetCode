import heapq as hq

class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """

        heap = []
        hq.heapify(heap)

        for point in points:
            dist_org = (abs(point[0]) * abs(point[0])) + (abs(point[1]) * abs(point[1]))
            hq.heappush(heap,[dist_org, point])

        res = []
        for x in range(k):
            point = hq.heappop(heap)
            res.append(point[1])

        return res

        