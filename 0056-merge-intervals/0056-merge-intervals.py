class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        n = len(intervals)
        res = []

        if n == 0:
            return res

        intervals = sorted(intervals)

        res.append(intervals[0])

        if n == 1:
            return res

        for x in range(1,n):
            interval1 = res.pop()
            interval2 = intervals[x]

            if interval1[1] >= interval2[0]:
                xc = min(interval1[0], interval2[0])
                yc = max(interval1[1], interval2[1])

                combined = [xc, yc]
                res.append(combined)
            else:
                res.append(interval1)
                res.append(interval2)

        return res
        