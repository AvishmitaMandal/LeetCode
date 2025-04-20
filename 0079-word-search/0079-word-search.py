class Solution:
    def wordSearchBacktrack(self, board, word, x, y, curr_idx, visited):
        m, n = len(board), len(board[0])
        if curr_idx == len(word)-1:
            return True
        
        visited.add((x,y))
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        for dx, dy in directions:
            new_x, new_y = x + dx, y + dy
            if new_x >= 0 and new_x < m and new_y >= 0 and new_y < n and (new_x,new_y) not in visited and board[new_x][new_y] == word[curr_idx+1]:
                visited.add((new_x, new_y))
                if self.wordSearchBacktrack(board, word, new_x, new_y, curr_idx+1, visited):
                    return True
                visited.remove((new_x, new_y))

        return False


    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        for x in range(m):
            for y in range(n):
                if board[x][y] == word[0]:
                    visited = set()
                    if self.wordSearchBacktrack(board, word, x, y, 0, visited):
                        return True

        return False

        