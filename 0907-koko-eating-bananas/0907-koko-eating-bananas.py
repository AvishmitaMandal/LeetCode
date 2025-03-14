class Solution:
    '''
    piles = 3,6,7,11]
    h = 8

    low = 4
    high = 3
    mid = 4

    time_taken = 1 + 2 + 2 + 3 = h
    ans = 4

    '''

    def calculateTime(self, piles, k):
        res = 0
        for pile in piles:
            res += ceil(pile/k)

        return res

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        n = len(piles)
        low, high = 1, max(piles)
        ans = high

        while low <= high:
            mid = (low + high)//2
            time_taken = self.calculateTime(piles, mid)

            if time_taken <= h:
                high = mid - 1
                ans = min(ans, mid)
            else:
                low = mid + 1

        return ans
        