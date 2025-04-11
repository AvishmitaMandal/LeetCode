class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        '''
        Example 1:

        Input: nums = [3,2,3]
        Output: 3

        Example 2:

        Input: nums = [2,2,1,1,1,2,2]
        Output: 2

        Approach 1
        [1,1,1,2,2,2,2]
        count = 4
        Sort - 
        Count - 

        TC: O(nlogn)
        SC: O(1)

        Approach 2
        [2,2,1,1,1,2,2]
        
        mp 
        2 - 4
        1 - 3

        TC: O(n)
        SC: O(n)

        '''

        count = 1
        ele = nums[0]
        for x in range(1, len(nums)):
            if count == 0:
                ele = nums[x]
                count += 1
            elif nums[x] == ele:
                count += 1
            else:
                count -= 1

        count = 0
        for num in nums:
            if num == ele:
                count += 1

        if count > len(nums)//2:
            return ele
                
        