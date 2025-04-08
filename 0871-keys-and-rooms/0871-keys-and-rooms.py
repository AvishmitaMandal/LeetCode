from collections import deque
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        q = deque()
        visited = set()
        n = len(rooms)

        q.append(0)

        while q:
            curr = q.popleft()
            visited.add(curr)

            for r in rooms[curr]:
                if r not in visited:
                    q.append(r)

        return n == len(visited)
            

        