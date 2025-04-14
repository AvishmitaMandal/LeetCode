class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        prefix, suffix = 1, 1
        res = -float("inf")

        n = len(nums)
        for x in range(n):
            prefix *= nums[x]
            suffix *= nums[n-1-x]
            res = max(res, prefix, suffix)

            if prefix == 0:
                prefix = 1
            if suffix == 0:
                suffix = 1

        return res


        