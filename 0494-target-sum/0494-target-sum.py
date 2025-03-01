class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total_sum = sum(nums)
        if target > total_sum or (total_sum-target) % 2 != 0:
            return 0
        

        k = (total_sum-target) // 2
        print(k)
        m, n = len(nums)+1, k+1

        dp = [[0 for _ in range(n)] for _ in range(m)]
        dp[0][0] = 1
        for j in range(1, m):
            if nums[j-1] == 0:
                dp[j][0] = 2 * dp[j-1][0]
            else:
                dp[j][0] = dp[j-1][0]

        for j in range(1, m):
            for i in range(1, n):
                dp[j][i] = dp[j-1][i]
                if i - nums[j-1] >= 0:
                    dp[j][i] += dp[j-1][i-nums[j-1]]

        print(dp)

        return dp[m-1][n-1]

        