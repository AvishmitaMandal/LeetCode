class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)

        dp = [0] * n
        for x in range(n):
            dp[x] = 1
            for y in range(x-1,-1,-1):
                if nums[y] < nums[x]:
                    dp[x] = max(dp[x], 1+dp[y])
                    

        print(dp)

        res = 0
        for x in range(n):
            res = max(res, dp[x])

        return res
            
        