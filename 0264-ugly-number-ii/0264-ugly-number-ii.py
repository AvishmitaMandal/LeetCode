import heapq

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        '''
        10 ,9, 15, 12, 20, 18, 30, 16, 24, 40  also a map

        1, 2, 3, 4, 5, 6, 8, 9
        '''

        hashmap = {}
        heap = []
        ugly_list = []

        heapq.heappush(heap, 1)
        hashmap[1] = 1

        while len(ugly_list) <= n:
            min_ele = heapq.heappop(heap)
            ugly_list.append(min_ele)
            if 2 * min_ele not in hashmap:
                heapq.heappush(heap, min_ele*2)
                hashmap[2 * min_ele] = 1
            if 3 * min_ele not in hashmap:
                heapq.heappush(heap, min_ele*3)
                hashmap[3 * min_ele] = 1
            if 5 * min_ele not in hashmap:
                heapq.heappush(heap, min_ele*5)
                hashmap[5 * min_ele] = 1
        print(ugly_list)
        return ugly_list[n-1]
        