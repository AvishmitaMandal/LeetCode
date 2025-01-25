class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        '''
        [
            [1,3,1],
            [1,5,1],
            [4,2,1]
            ]

        [
            [1,4,5],
            [2,7,6],
            [6,8,7]
            ]
        '''

        m, n = len(grid), len(grid[0])
        dp = [[0]*n for _ in range(m)]

        dp[0][0] = grid[0][0]
        for x in range(1, n):
            dp[0][x] = dp[0][x-1] + grid[0][x]

        for y in range(1, m):
            dp[y][0] = dp[y-1][0] + grid[y][0]

        print(dp)

        for y in range(1,m):
            for x in range(1, n):
                dp[y][x] = min(dp[y-1][x], dp[y][x-1]) + grid[y][x]

        return dp[m-1][n-1]
        