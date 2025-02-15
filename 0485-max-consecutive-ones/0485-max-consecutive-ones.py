'''
1,1,0,1,1,1
          
'''

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count, max_count = 0, 0
        for num in nums:
            if num == 1:
                count += 1
            else:
                max_count = max(max_count, count)
                count = 0
                
        max_count = max(max_count, count)
        return max_count
                

        