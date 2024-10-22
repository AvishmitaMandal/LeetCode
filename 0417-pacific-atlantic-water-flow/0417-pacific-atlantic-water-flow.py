class Solution:
    def bfs(self, x, y, heights):
        m,n = len(heights), len(heights[0])
        top_right, bottom_left = (0,m-1), (n-1,0)
        P_flag, A_flag = False, False
        
        q = deque()
        q.append((x, y))

        visited_set = set()
        visited_set.add((x, y))

        directions = ((1,0), (-1,0), (0,1), (0,-1))
        while q:
            cx, cy = q.popleft()
            cord = (cx, cy)
            if x == 0 and y == 13:
                print(m)
                print(n)
            if cx == 0 or cy == 0:
                P_flag = True
            if cx == m-1 or cy == n-1:
                A_flag = True
            if P_flag and A_flag:
                return True

            for dx, dy in directions:
                nx, ny = cx+dx, cy+dy
                if 0 <= nx < m and 0 <= ny <n and heights[cx][cy] >= heights[nx][ny] and (nx, ny) not in visited_set:
                    visited_set.add((nx, ny))
                    q.append((nx,ny))

        return False




    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m,n = len(heights), len(heights[0])
        res = []

        for x in range(m):
            for y in range(n):
                if self.bfs(x, y, heights):
                    temp = []
                    temp.append(x)
                    temp.append(y)
                    res.append(temp)

        return res
        