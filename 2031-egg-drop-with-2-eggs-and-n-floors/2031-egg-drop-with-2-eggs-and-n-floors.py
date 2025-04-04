class Solution:
    def solve(self, e, f, dp):
        if f == 1 or f == 0:
            return f

        if e == 1:
            return f

        if dp[e][f] != -1:
            return dp[e][f]

        ans = 10**5
        for k in range(1, f+1):
            b, nb = -1, -1
            if dp[e-1][k-1] != -1:
                b = dp[e-1][k-1]
            else:
                b = self.solve(e-1, k-1, dp)
                dp[e-1][k-1] = b

            if dp[e][f-k] != -1:
                nb = dp[e][f-k]
            else:
                nb = self.solve(e, f-k, dp)
                dp[e][f-k] = nb

            temp = 1 + max(b,nb)
            ans = min(temp, ans)

        dp[e][f] = ans
        return ans

    def twoEggDrop(self, n: int) -> int:

        dp = [[-1 for _ in range(n+1)] for _ in range(3)]
        # print(dp)
        return self.solve(2, n, dp)