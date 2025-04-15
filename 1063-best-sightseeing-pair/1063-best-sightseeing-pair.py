class Solution:
    def maxScoreSightseeingPair(self, nums: List[int]) -> int:
        n = len(nums)
        start, end = [], []

        MIN = -float("inf")
        end.append(MIN)
        start.append(nums[0])

        for x in range(1, n):
            if x == n-1:
                start.append(MIN)
            else:
                start.append(nums[x]+x)
            end.append(nums[x]-x)

        max_start_left = [MIN]
        max_val = nums[0]

        for x in range(1, n):
            max_start_left.append(max_val)
            max_val = max(max_val,start[x])

        res = MIN
        for x in range(n):
            res = max(res, max_start_left[x]+end[x])

        return res

        



        