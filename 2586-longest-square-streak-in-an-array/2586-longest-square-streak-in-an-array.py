class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        mp = {}
        n = len(nums)

        nums.sort(reverse = True)
        res = 1

        for x in range(n):
            sq = nums[x] * nums[x]
            if sq in mp:
                mp[nums[x]] = mp[sq]+1
                res = max(res, mp[nums[x]])
            else:
                mp[nums[x]] = 1

        if res < 2:
            return -1
        return res

        