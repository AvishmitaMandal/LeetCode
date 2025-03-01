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
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        n = len(accounts)
        dj = DisjointSet(n)
        email_mp = {}

        for x in range(n):
            account = accounts[x]
            for y in range(1, len(account)):
                if account[y] not in email_mp:
                    email_mp[account[y]] = x
                else:
                    up = dj.findUPar(email_mp[account[y]])
                    uv = dj.findUPar(x)
                    dj.unionBySize(up, uv)

        res_mp = {}
        for key, val in email_mp.items():
            val = dj.findUPar(val)
            if val in res_mp:
                res_mp[val].append(key)
            else:
                res_mp[val] = [key]

        res = []

        for key, val in res_mp.items():
            sorted_val = sorted(val)
            name = accounts[key][0]
            temp = [name]
            temp = temp + sorted_val
            res.append(temp)

        return res
                

        