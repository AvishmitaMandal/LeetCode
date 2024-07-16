class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        grid = [[1 for x in range(n)] for y in range(m)]
        grid[0][0] = 1
        
        for i in range(1,m):
            for j in range(1,n):
                grid[i][j] = grid[i-1][j] + grid[i][j-1]

        return grid[m-1][n-1]
        