from collections import deque
class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        un_adj_list = {}
        adj_list = {}
        for n1, n2 in connections:
            if n1 in un_adj_list:
                un_adj_list[n1].append(n2)
            else:
                un_adj_list[n1] = [n2]

            if n2 in un_adj_list:
                un_adj_list[n2].append(n1)
            else:
                un_adj_list[n2] = [n1]

            if n2 in adj_list:
                adj_list[n2].append(n1)
            else:
                adj_list[n2] = [n1]
        
        q = deque()
        q.append(0)
        visited = set()
        count = 0

        while q:
            curr = q.popleft()
            visited.add(curr)
            if curr in adj_list:
                for x in range(len(adj_list[curr])):
                    if adj_list[curr][x] not in visited:
                        q.append(adj_list[curr][x])
                        visited.add(adj_list[curr][x])
            if curr in un_adj_list:
                for x in range(len(un_adj_list[curr])):
                    if un_adj_list[curr][x] not in visited:
                        q.append(un_adj_list[curr][x])
                        visited.add(un_adj_list[curr][x])
                        count += 1

        return count





        