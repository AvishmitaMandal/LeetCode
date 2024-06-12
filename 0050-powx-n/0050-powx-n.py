class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        elif n == 1:
            return x
        elif n == -1:
            return 1 / x

        k = self.myPow(x, n//2)

        if n%2 == 0:
            return k * k
        else:
            return x * k * k
        