class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        '''
            [10,5,2,6]    
        '''

        start, end = 0, 0
        count = 0
        product = 1

        if k < 1:
            return 0

        while end < len(nums):
            product *= nums[end]

            while start <= end and product >= k:
                product /= nums[start]
                start += 1

            count += end - start + 1 
            end += 1

        return count

        