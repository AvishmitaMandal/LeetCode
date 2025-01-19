class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        start, end = 0, 0
        maxLength = 0
        countZero = 0

        while end < len(nums):
            if nums[end] == 0:
                countZero += 1
                if countZero > 1:
                    while start < end and nums[start] == 1:
                        start += 1
                    countZero -= 1
                    start += 1
            
            maxLength = max(maxLength, end-start+1)
            end += 1

        return maxLength - 1
        