import heapq

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        '''
        10 ,9, 15, 12, 20, 18, 30, 16, 24, 40  also a map

        1, 2, 3, 4, 5, 6, 8, 9
        '''

        seen = set()
        heap = []

        heapq.heappush(heap, 1)
        seen.add(1)
        primes = [2, 3, 5]
        min_ele = 0

        for _ in range(n):
            min_ele = heapq.heappop(heap)
            for prime in primes:
                next_ugly = prime * min_ele
                if next_ugly not in seen:
                    heapq.heappush(heap, next_ugly)
                    seen.add(next_ugly)


        return min_ele
        