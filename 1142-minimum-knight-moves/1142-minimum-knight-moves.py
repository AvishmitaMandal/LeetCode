from collections import deque
class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        moves = [(-1,-2),(-2,-1),(-2,1),(-1,2),(1,2),(2,1),(2,-1),(1,-2)]
        q = deque()
        q.append((0,0))
        level = -1
        visited = set()
        visited.add((0,0))

        while q:
            level += 1
            for i in range(len(q)):
                cx, cy = q.popleft()
                if cx == x and cy == y:
                    return level
                visited.add((cx,cy))
                for dx, dy in moves:
                    new_x, new_y = cx+dx, cy+dy
                    if (new_x, new_y) not in visited:
                        q.append((new_x, new_y))
                        visited.add((new_x, new_y))

        return 0





        