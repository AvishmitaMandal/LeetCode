import math

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        ele1, ele2 = 10**10, 10**10
        count1, count2 = 0, 0

        for x in range(0,len(nums)):
            if count1 == 0 and nums[x] != ele2:
                ele1 = nums[x]
                count1 = 1
            elif count2 == 0 and nums[x] != ele1:
                ele2 = nums[x]
                count2 = 1
            elif nums[x] == ele1:
                count1 += 1
            elif nums[x] == ele2:
                count2 += 1
            else:
                count1 -= 1
                count2 -= 1

        res_list = []
        
        count1, count2 = 0, 0
        for num in nums:
            if num == ele1:
                count1 += 1
            elif num == ele2:
                count2 += 1

        target = math.floor(len(nums)/3)

        if count1 > target:
            res_list.append(ele1)

        if count2 > target:
            res_list.append(ele2)

        return res_list
        