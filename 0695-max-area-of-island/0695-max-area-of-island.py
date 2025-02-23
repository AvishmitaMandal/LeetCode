from collections import deque
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        max_area = 0
        directions = [[0,1],[0,-1],[1,0],[-1,0]]

        q = deque()

        for y in range(m):
            for x in range(n):
                if grid[y][x] == 1:
                    q.append((x,y))
                    grid[y][x] = 0
                    count = 0
                    while q:
                        (curr_x, curr_y) = q.popleft()
                        count += 1
                        for dx, dy in directions:
                            new_x, new_y = curr_x + dx, curr_y + dy
                            if new_x >= 0 and new_y >= 0 and new_x < n and new_y < m and grid[new_y][new_x] == 1:
                                grid[new_y][new_x] = 0
                                q.append((new_x, new_y))
                    max_area = max(max_area, count)


        return max_area
                        


        