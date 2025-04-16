class Solution:
    def isOverlap(self, prev, curr):
        return prev[1] >= curr[0]

    def mergedInterval(self, prev, curr):
        return [min(prev[0], curr[0]), max(prev[1], curr[1])]

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        n = len(intervals)

        res = []
        prev_interval = intervals[0]
        for x in range(1, n):
            curr_interval = intervals[x]
            if self.isOverlap(prev_interval, curr_interval):
                new_interval = self.mergedInterval(prev_interval, curr_interval)
                prev_interval = new_interval
            else:
                res.append(prev_interval)
                prev_interval = curr_interval
        res.append(prev_interval)

        return res

            


        