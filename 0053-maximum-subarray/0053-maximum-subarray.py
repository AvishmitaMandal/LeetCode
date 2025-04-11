class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = -10**10
        total = 0

        for x in range(len(nums)):
            total += nums[x]
            max_sum = max(max_sum, total)
            total = max(0, total)

        return max_sum
        