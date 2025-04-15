class Solution:
    def maxScoreSightseeingPair(self, nums: List[int]) -> int:
        MIN = -float("inf")
        n = len(nums)

        max_start = nums[0]
        res = MIN

        for x in range(1, n):
            res = max(res, max_start + nums[x]-x)
            max_start = max(max_start, nums[x]+x)

        return res
        