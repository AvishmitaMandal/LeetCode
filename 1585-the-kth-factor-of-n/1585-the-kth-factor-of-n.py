import math
class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        factors_list = []
        for x in range(1, math.floor(math.sqrt(n))+1):
            if n % x == 0:
                factors_list.append(x)

        m = len(factors_list)
        if m >= k:
            return factors_list[k-1]

        for x in range(m-1, -1, -1):
            fact = n // factors_list[x]
            if fact not in factors_list:
                factors_list.append(fact)

        if len(factors_list) >= k:
            return factors_list[k-1]

        return -1


        