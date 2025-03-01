class DisjointSet:
    def __init__(self, n: int):
        self.par = [i for i in range(n)]
        self.size = [1 for _ in range(n)]

    def findUPar(self, u: int):
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
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        num_compo = 0
        dj = DisjointSet(n)
        
        for edge in edges:
            dj.unionBySize(edge[0], edge[1])

        for x in range(len(dj.par)):
            if x == dj.par[x]:
                num_compo += 1

        return num_compo



        