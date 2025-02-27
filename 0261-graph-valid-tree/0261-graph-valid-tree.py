from collections import deque

class Solution:
    def is_cycle(self, adj_list, n, visited):
        q = deque()
        q.append((0, -1))

        while q:
            (curr, par) = q.popleft()
            visited[curr] = 1

            if curr in adj_list:
                for adj_node in adj_list[curr]:
                    if adj_node == par:
                        continue
                    if visited[adj_node] == 1:
                        return True
                    q.append((adj_node, curr))

        return False


    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # create adj list
        adj_list = {}

        for edge in edges:
            if edge[0] in adj_list:
                adj_list[edge[0]].append(edge[1])
            else:
                adj_list[edge[0]] = [edge[1]]

            if edge[1] in adj_list:
                adj_list[edge[1]].append(edge[0])
            else:
                adj_list[edge[1]] = [edge[0]]

        visited = [0 for _ in range(n)]

        if self.is_cycle(adj_list, n, visited):
            return False

        for visited_node in visited:
            if visited_node == 0:
                return False

        return True

        


        