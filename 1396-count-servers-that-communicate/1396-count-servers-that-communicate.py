class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        n_row, n_col = len(grid), len(grid[0])
        server_count = 0

        for x in range(n_row):
            for y in range(n_col):
                if grid[x][y] != 0:
                    # check row
                    flag = 0
                    for i in range(n_col):
                        if i == y:
                            continue
                        if grid[x][i] != 0:
                            flag = 1
                        if grid[x][i] == 1:
                            grid[x][i] = 2
                            server_count += 1
                    # check column
                    for j in range(n_row):
                        if j == x:
                            continue
                        if grid[j][y] != 0:
                            flag = 1
                        if grid[j][y] == 1:
                            grid[j][y] = 2
                            server_count += 1
                    if grid[x][y] == 1 and flag == 1:
                        grid[x][y] = 2
                        server_count += 1

        return server_count
                
        