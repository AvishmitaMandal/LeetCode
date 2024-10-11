class Solution:
    def fib(self, n: int) -> int:
        fib_list = []
        fib_list.append(0)
        fib_list.append(1)

        if n==0 or n==1:
            return n

        for x in range(2, n+1):
            fib_list.append(fib_list[x-1]+ fib_list[x-2])

        return fib_list[n]
        