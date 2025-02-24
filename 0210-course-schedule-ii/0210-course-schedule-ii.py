from collections import deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        in_degree = [0 for _ in range(numCourses)]
        adj_list = {}

        for p in prerequisites:
            in_degree[p[0]] += 1
            if p[1] in adj_list:
                adj_list[p[1]].append(p[0])
            else:
                adj_list[p[1]] = [p[0]]

        q = deque()

        for x in range(numCourses):
            if in_degree[x] == 0:
                q.append(x)

        res = []

        while q:
            curr = q.popleft()
            res.append(curr)
            if curr in adj_list:
                for neighbor in adj_list[curr]:
                    in_degree[neighbor] -= 1
                    if in_degree[neighbor] == 0:
                        q.append(neighbor)
        
        if len(res) != numCourses:
            return []

        return res



        

        