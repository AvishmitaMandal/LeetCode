class Solution:
    def connectedComponents(self, x, y, board):
        m, n = len(board), len(board[0])
        q = deque()
        q.append((x,y))

        visited_set = set()
        visited_set.add((x,y))

        directions = ((0,1),(0,-1),(1,0),(-1,0))

        while q:
            cx, cy = q.popleft()

            for dx,dy in directions:
                nx, ny = cx+dx, cy+dy
                if 0 <= nx < m and 0 <= ny < n and (nx,ny) not in visited_set and board[nx][ny] == 'O':
                    q.append((nx,ny))
                    visited_set.add((nx,ny))

        return visited_set

    def isSurrounded(self, comp, board):
        m, n = len(board), len(board[0])
        isSurrounded = True
        directions = ((0,1),(0,-1),(1,0),(-1,0))

        for x,y in comp:
            for dx,dy in directions:
                nx, ny = x+dx, y+dy
                if not (0 <= nx < m and 0 <= ny < n):
                    isSurrounded = False
                    return isSurrounded

        return isSurrounded

    def updateBoard(self, comp, board):
        for x,y in comp:
            board[x][y] = 'X'

        return board


    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])

        for x in range(m):
            for y in range(n):
                if board[x][y] == 'O':
                    comp = self.connectedComponents(x, y, board)
                    if self.isSurrounded(comp, board):
                        board = self.updateBoard(comp, board)
        