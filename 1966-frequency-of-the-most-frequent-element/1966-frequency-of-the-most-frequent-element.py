class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        '''
        [3,9,4,6] k = 5
        [3,4,6,9]
        '''
        sorted_nums = sorted(nums)
        prev_sum = sorted_nums[0]
        start, end = 0, 1
        max_length = 1

        while end <len(sorted_nums):
            
            while start <= end and (end-start)*sorted_nums[end] - prev_sum > k:
                prev_sum -= sorted_nums[start]
                start += 1

            max_length = max(max_length, end-start + 1)
            prev_sum += sorted_nums[end]

            end += 1

        return max_length
        
            

        