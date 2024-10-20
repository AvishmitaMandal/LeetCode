from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m,n = len(grid), len(grid[0])
        q = deque()

        good = 0
        for x in range(m):
            for y in range(n):
                if grid[x][y] == 2:
                    q.append((x,y))
                elif grid[x][y] == 1:
                    good += 1

        if good == 0:
            return 0

        directions = ((1,0),(-1,0),(0,1),(0,-1))
        time = -1
        while q:
            qlen = len(q)
            for x in range(qlen):
                cx, cy = q.popleft()
                for dx, dy in directions:
                    nx, ny = cx+dx, cy+dy
                    if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == 1:
                        grid[nx][ny] = 2
                        q.append((nx,ny))
            time += 1

        

        for x in range(m):
            for y in range(n):
                if grid[x][y] == 1:
                    return -1

        return time 



        
        