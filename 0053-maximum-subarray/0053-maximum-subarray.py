class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = - 2**31

        sum_num = 0
        for num in nums:
            sum_num += num
            res = max(res, sum_num)

            if sum_num < 0:
                sum_num = 0

        return res
        