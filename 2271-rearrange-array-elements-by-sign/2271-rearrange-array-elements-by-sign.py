class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pos, neg = 0, 1
        ans = [0] * n

        for x in range(n):
            if nums[x] > 0:
                ans[pos] = nums[x]
                pos += 2
            else:
                ans[neg] = nums[x]
                neg += 2

        return ans


        