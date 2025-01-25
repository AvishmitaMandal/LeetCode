class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        '''
        1, 2, 3, 4, 5, 6, 7, 8, 9,10,11
        1, 1, 2, 2, 1, 2, 2, 3, 3, 2, 3
        0, -1, -1, -1
        '''
        dp = [-1]*(amount + 1)
        dp[0] = 0

        for x in range(1, amount+1):
            min_count = amount + 1
            for coin in coins:
                if x - coin >= 0 and dp[x-coin] != -1:
                    min_count = min(min_count, dp[x-coin]+1)
            if min_count != amount+1:
                dp[x] = min_count

        print(dp)

        return dp[amount]



        