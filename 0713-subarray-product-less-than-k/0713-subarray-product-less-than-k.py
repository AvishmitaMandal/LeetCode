class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        
        count = 0
        start, end = 0, 0

        curr_prod = 1

        while end < len(nums):
            curr_prod *= nums[end]

            while start <= end  and curr_prod >= k:
                curr_prod = curr_prod // nums[start]
                start += 1

            count += (end-start+1)
            end += 1

        return count
        