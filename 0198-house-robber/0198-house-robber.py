class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * n
        dp[0] = nums[0]

        for x in range(1, n):
            curr_steal = nums[x]
            if x-2 >= 0:
                curr_steal += dp[x-2]

            prev_steal = dp[x-1]
            dp[x] = max(curr_steal, prev_steal)

        return dp[n-1]

        