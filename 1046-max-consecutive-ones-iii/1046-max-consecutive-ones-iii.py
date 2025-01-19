class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        '''
        nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
        '''

        count_zeroes = 0
        max_length = 0

        start, end = 0, 0

        while end < len(nums):
            if nums[end] == 0:
                count_zeroes += 1
                if count_zeroes > k:
                    while start < end and nums[start] != 0 :
                        start += 1
                    count_zeroes -= 1
                    start += 1

            max_length = max(max_length, end-start+1)
            end += 1

        return max_length
        