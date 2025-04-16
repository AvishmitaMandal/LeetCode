from collections import deque
class Solution:
    def isWithinBounds(self, x, y, m, n):
        return x >= 0 and x < m and y >=0 and y < n

    def bfsTraversal(self, heights, q, visited):
        m, n = len(heights), len(heights[0])
        directions = [(0,1), (0,-1), (1,0), (-1,0)]

        while q:
            curr_x, curr_y = q.popleft()
            visited[curr_x][curr_y] = 1
            for dx, dy in directions:
                new_x, new_y = curr_x + dx, curr_y + dy
                if self.isWithinBounds(new_x, new_y, m, n) and visited[new_x][new_y] == 0 and heights[new_x][new_y] >= heights[curr_x][curr_y]:
                    q.append((new_x, new_y))
                    visited[new_x][new_y] = 1
        
        return visited


    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])

        q = deque()
        visited_pacific = [[0 for _ in range(n)] for _ in range(m)]
        for y in range(n):
            q.append((0,y))
            visited_pacific[0][y] = 1
        for x in range(1, m):
            q.append((x,0))
            visited_pacific[x][0] = 1

        visited_p = self.bfsTraversal(heights, q, visited_pacific)
        print(visited_p)

        q = deque()
        visited_atlantic = [[0 for _ in range(n)] for _ in range(m)]
        for y in range(n):
            q.append((m-1,y))
            visited_atlantic[m-1][y] = 1
        for x in range(m-1):
            q.append((x,n-1))
            visited_atlantic[x][n-1] = 1

        visited_atlantic = self.bfsTraversal(heights, q, visited_atlantic)

        res = []
        for x in range(m):
            for y in range(n):
                if visited_pacific[x][y] and visited_atlantic[x][y]:
                    res.append([x,y])

        return res
        