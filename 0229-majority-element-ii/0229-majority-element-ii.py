class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        DUMMY_VAL = float("inf")
        n = len(nums)
        if n == 1:
            return nums

        ele1, ele2 = DUMMY_VAL, DUMMY_VAL
        count1, count2 = 0, 0

        for x in range(n):
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

            

        print(ele1, ele2)

        res = []
        target = n//3
        ele1_count, ele2_count = 0, 0

        # Check for ele1
        for x in range(n):
            if nums[x] == ele1:
                ele1_count += 1
            if nums[x] == ele2:
                ele2_count += 1
        print(target)

        if ele1_count > target:
            res.append(ele1)
        if ele2_count > target:
            res.append(ele2)

        return res

                    

        