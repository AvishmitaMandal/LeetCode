from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        count = 0
        directions = [[0,1], [0,-1], [1,0], [-1,0]]

        q = deque()
        for j in range(m):
            for i in range(n):
                if grid[j][i] == "1":
                    q.append((j, i))
                    grid[j][i] = "0"
                    while q:
                        (curr_loc_j, curr_loc_i) = q.popleft()
                        for di, dj in directions:
                            new_i = curr_loc_i + di
                            new_j = curr_loc_j + dj
                            if new_i >= 0 and new_i < n and new_j >=0 and new_j < m and grid[new_j][new_i] == "1":
                                grid[new_j][new_i] = "0"
                                q.append((new_j, new_i))
                    count += 1

        return count




        