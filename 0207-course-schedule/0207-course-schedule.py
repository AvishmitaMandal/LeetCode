from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        count = 0
        indegrees = [0] * numCourses
        adj_list = {}

        for prerequisite in prerequisites:
            a, b = prerequisite[0], prerequisite[1]
            indegrees[a] += 1

            if b in adj_list:
                adj_list[b].append(a)
            else:
                adj_list[b] = [a]

        q = deque()
        visited = set()
        for x in range(numCourses):
            if indegrees[x] == 0:
                q.append(x)

        while q:
            curr = q.popleft()
            visited.add(curr)
            count += 1

            if curr in adj_list:
                for neighbor in adj_list[curr]:
                    indegrees[neighbor] -= 1
                    if indegrees[neighbor] == 0 and neighbor not in visited:
                        q.append(neighbor)
                        visited.add(neighbor)

        print(count)
        return count == numCourses



        


        