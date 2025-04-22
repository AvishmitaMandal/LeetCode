class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        count = 0
        for x in range(1, n+1):
            if n % x == 0:
                count += 1
                if count == k:
                    return x

        return -1
        