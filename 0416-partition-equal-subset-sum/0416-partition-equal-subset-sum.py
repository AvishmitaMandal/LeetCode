class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        '''
        [1,5,11,5]
        '''
        total_sum = 0
        for num in nums:
            total_sum += num

        if total_sum % 2 != 0:
            return False

        target = total_sum//2
        n = len(nums)
        dp = [[False]*(target + 1) for _ in range(n+1)]

        for j in range(n+1):
            dp[j][0] = True

        for j in range(1, n+1):
            for i in range(1, target+1):
                if dp[j-1][i] == True:
                    dp[j][i] = True
                elif i-nums[j-1]>= 0 and dp[j-1][i-nums[j-1]]:
                    dp[j][i] = True

        return dp[n][target]