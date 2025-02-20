class Solution:
    def my_pow_util(self, x, n):
        if n == 1:
            return x

        num = self.my_pow_util(x*x,n//2)
        print(num)

        if n%2 == 0:
            return num

        return x * num

    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            x = (1/x)
            n *= -1
        
        if n==0:
            return 1

        num = self.my_pow_util(x, n)
        return num
        