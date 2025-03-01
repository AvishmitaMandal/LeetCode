class DisjointSet:
    def __init__(self, n: int):
        self.par = [-1 for x in range(n)]
        self.size = [1 for _ in range(n)]

    def findUPar(self, u: int) -> int:
        if u == self.par[u]:
            return u
        self.par[u] = self.findUPar(self.par[u])
        return self.par[u]

    def unionBySize(self, u: int, v: int):
        up = self.findUPar(u)
        vp = self.findUPar(v)

        if up == vp:
            return
        
        if self.size[up] > self.size[vp]:
            self.size[up] += self.size[vp]
            self.par[vp] = up
        else:
            self.size[vp] += self.size[up]
            self.par[up] = vp

        return 

class Solution:
    def num_compo(self, par: List[int]) -> int:
        count = 0
        for x in range(len(par)):
            if x == par[x]:
                count += 1
        
        return count

    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        directions = [[0,1], [1,0], [-1,0], [0,-1]]
        num = len(positions)

        dj = DisjointSet(num)
        mp = {}

        for x in range(len(positions)):
            mp[tuple(positions[x])] = x

        new_mp = {}
        res = []

        for position in positions:
            new_mp[tuple(position)] = mp[tuple(position)]
            dj.par[mp[tuple(position)]] = mp[tuple(position)]

            for dx, dy in directions:
                new_y, new_x = position[0]+dy, position[1]+dx
                new_position = [new_y, new_x] 
                if new_x >= 0 and new_x < n and new_y >=0 and new_y < m and tuple(new_position) in new_mp:
                    # print("new_position : ", new_position)
                    u = mp[tuple(position)]
                    v = mp[tuple(new_position)]
                    dj.unionBySize(u, v)
            
            # print(dj.par)
            num = self.num_compo(dj.par)
            res.append(num)

        return res




        