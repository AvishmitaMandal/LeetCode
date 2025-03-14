class Solution:
    def calculateBouquet(self, bloomDay: List[int], day: int, k: int):
        n = len(bloomDay)
        isBloom = [0 for _ in range(n)]

        res, cnt = 0, 0
        for x in range(n):
            if day >= bloomDay[x]:
                cnt += 1
            else:
                res += (cnt//k)
                cnt = 0

        res += (cnt//k)
        return res
            


    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        low, high = 1, max(bloomDay)
        ans = 10**9+1

        if m*k > len(bloomDay):
            return -1

        while low <= high:
            mid = (low + high)//2

            num_bouquet = self.calculateBouquet(bloomDay, mid, k)
            if num_bouquet >= m:
                ans = min(ans, mid)
                high = mid - 1
            else:
                low = mid + 1

        if ans == 10**9+1:
            return -1

        return ans
        