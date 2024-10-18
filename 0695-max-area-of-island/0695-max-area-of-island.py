class Solution:
    def bfs(self, x, y, grid):
        m = len(grid)
        n = len(grid[0])

        q = deque()
        q.append((x,y))
        area = 0
        directions = [(1,0), (0,1), (-1,0), (0,-1)]

        while q:
            cord = q.popleft()
            print(type(cord))
            print(cord)
            x, y = cord
            area += 1
            for dx, dy in directions:
                new_x, new_y = x+dx, y+dy
                if 0 <= new_x < m and 0 <= new_y < n and grid[new_x][new_y] == 1:
                    grid[new_x][new_y] = 0
                    q.append((new_x, new_y))

        return area



    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        max_area = 0

        for x in range(m):
            for y in range(n):
                if grid[x][y] == 1:
                    grid[x][y] = 0
                    area = self.bfs(x,y,grid)
                    max_area = max(max_area, area)

        return max_area
        