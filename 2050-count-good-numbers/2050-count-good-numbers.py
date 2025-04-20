class Solution:
    def pow(self, x, n):
        MOD = 10**9 + 7
        if n == 1:
            return x
        if n == 0:
            return 1

        k = self.pow(x, n//2)
        if n%2 == 0:
            return (k * k) % MOD
        else:
            return (x * k * k) % MOD

    def countGoodNumbers(self, n: int) -> int:
        MOD = 10**9 + 7
        
        odd_places = n//2
        even_places = n-odd_places

        ans = 1
        odd = self.pow(4, odd_places) % MOD
        even = self.pow(5, even_places) % MOD
        ans *= (odd * even) % MOD
        return ans