from collections import deque, defaultdict
class Solution:
    def isValid(self, x, y, n):
        return x >= 0 and x < n and y >= 0 and y < n

    def findComponents(self, x, y, grid, visited):
        n = len(grid)
        neighbouring_water = set()
        directions = [(0,1), (1,0), (0,-1), (-1,0)]
        q = deque()
        q.append((x, y))
        visited[x][y] = True

        component_size = 0
        while q:
            curr_x, curr_y = q.popleft()
            component_size += 1
            for dx, dy in directions:
                new_x = curr_x + dx
                new_y = curr_y + dy
                if self.isValid(new_x, new_y, n):
                    if grid[new_x][new_y] == 1 and not visited[new_x][new_y]:
                        q.append((new_x, new_y))
                        visited[new_x][new_y] = True
                    elif grid[new_x][new_y] == 0:
                        neighbouring_water.add((new_x, new_y))

        return component_size, neighbouring_water


    def largestIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if n == 0:
            return 0

        visited = [[False for _ in range(n)] for _ in range(n)]

        island_info_list = []

        for x in range(n):
            for y in range(n):
                if grid[x][y] == 1 and not visited[x][y]:
                    component_size, neighbouring_water = self.findComponents(x, y, grid, visited)
                    island_info_list.append((component_size, neighbouring_water))

        island_info_list.sort(reverse = True)
        m = len(island_info_list)
        
        if m == 0:
            return 1

        if m == 1:
            size, neigh = island_info_list[0]
            if len(neigh) == 0:
                return size
            return size + 1

        # print(island_info_list)
        mp = defaultdict(int)
        
        for i in range(m):
            size, neighbs = island_info_list[i]
            neighbs = list(neighbs)
            for neighb in neighbs:
                mp[neighb] += size

        ans = 0
        for key, val in mp.items():
            ans = max(ans, val)
            
        return ans + 1





        