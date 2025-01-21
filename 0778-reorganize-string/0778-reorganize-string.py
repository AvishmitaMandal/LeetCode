from collections import defaultdict
import heapq

class Solution:
    def reorganizeString(self, s: str) -> str:
        '''
        s = "aaab"
        a - 3
        b - 1

        s = "aaabbca"
        a - 4
        b - 2
        c - 1
        ababaca

        s = "aabbcca"
        a - 3
        b - 2
        c - 2
        abcabca
        '''
        frequency = defaultdict(int)
        for c in s:
            frequency[c] += 1

        heap = []
        for key, val in frequency.items():
            heapq.heappush(heap, (-val, key))

        print(heap)

        res = []
        for _ in range(len(s)):
            # first element
            if len(res) == 0:
                val, key = heapq.heappop(heap)
                print(heap)
                val *= -1
                res.append(key)
                prev_element = key
                val -= 1
                if val != 0:
                    heapq.heappush(heap, (-val, key))
                    print(heap)
            else:
                val, key = heapq.heappop(heap)
                val *= -1
                print(heap)
                if prev_element == key:
                    if not heap:
                        return ""
                    else:
                        val2, key2 = heapq.heappop(heap)
                        print(heap)
                        val2 *= -1
                        res.append(key2)
                        prev_element = key2
                        val2 -= 1
                        if val2 != 0:
                            heapq.heappush(heap, (-val2, key2))
                            print(heap)
                        heapq.heappush(heap, (-val, key))
                        print(heap)

                else:
                    res.append(key)
                    prev_element = key
                    val -= 1 
                    if val != 0:
                        heapq.heappush(heap, (-val, key))

        return ''.join(res)


        




        