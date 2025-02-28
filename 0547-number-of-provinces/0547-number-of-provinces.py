class DisjointSet:
        def __init__(self, n: int):
            self.size = [0 for _ in range(n)]
            self.par = [i for i in range(n)]

        def findUPar(self, u: int):
            if u == self.par[u]:
                return u
            self.par[u] = self.findUPar(self.par[u])
            return self.par[u]


        def unionBySize(self, u: int, v: int):
            up = self.findUPar(u)
            vp = self.findUPar(v)

            if self.size[up] > self.size[vp]:
                self.par[vp] = up
                self.size[up] += self.size[vp]
            else:
                self.par[up] = vp
                self.size[vp] += self.size[up]
            return

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
    
        n = len(isConnected)
        dj = DisjointSet(n)

        for j in range(1, n):
            for i in range(j):
                if isConnected[j][i] == 1:
                    dj.unionBySize(j, i)

        count = 0

        for x in range(n):
            if dj.par[x] == x:
                count += 1

        return count

