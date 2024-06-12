import math

class Solution:
    def isSufficient(self, mid, h, piles):
        res = 0
        for pile in piles:
            res += math.ceil(pile/mid)   

        if res <= h:
            return True

        return False

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        len_piles = len(piles)

        max_pile, min_pile, sum_piles = 0, 10**10, 0
        for pile in piles:
            max_pile = max(max_pile, pile)
            min_pile = min(min_pile, pile)
            sum_piles += pile

        if h == len_piles:
            return max_pile

        if h >= sum_piles:
            return 1

        res = 0
        start, end = 1, max_pile
        while start <= end:
            mid = (start + end)//2

            if self.isSufficient(mid, h, piles):
                res = mid
                end = mid-1 
            else:
                start = mid+1
        
        return res



        