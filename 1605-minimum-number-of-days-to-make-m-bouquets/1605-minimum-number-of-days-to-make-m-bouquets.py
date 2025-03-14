class Solution:
    def calculateBouquet(self, bloomDay: List[int], day: int, k: int):
        n = len(bloomDay)
        isBloom = [0 for _ in range(n)]

        for x in range(n):
            if day >= bloomDay[x]:
                isBloom[x] = 1

        # num of k consequtive 1s
        res = 0
        start, end = 0, 0
        while end < n:
            if isBloom[start] == 0:
                start += 1
                end += 1
                continue
            if isBloom[end] == 0:
                start = end

            size = end - start + 1
            if size == k:
                res += 1
                start = end + 1
                end = start-1
            end += 1

        # print("day : ", day)
        # print("isBloom : ", isBloom)
        # print("res : ", res)

        return res
            


    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        low, high = 1, max(bloomDay)
        ans = 10**9+1

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
        