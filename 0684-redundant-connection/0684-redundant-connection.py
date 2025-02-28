class DisjointSet:
    def __init__(self, n: int):
        self.par = [i for i in range(n+1)]
        self.size = [1 for _ in range(n+1)]

    def findUPar(self, u: int):
        if u == self.par[u]:
            return u
        self.par[u] = self.findUPar(self.par[u])
        return self.par[u]

    def unionBySize(self, u: int, v: int):
        up = self.findUPar(u)
        vp = self.findUPar(v)

        if up == vp:
            return True

        if self.size[up] > self.size[vp]:
            self.size[up] += self.size[vp]
            self.par[vp] = up
        else:
            self.size[vp] += self.size[up]
            self.par[up] = vp

        return False

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        dj = DisjointSet(n)

        for edge in edges:
            res = dj.unionBySize(edge[0], edge[1])
            if res:
                return edge

        return
        