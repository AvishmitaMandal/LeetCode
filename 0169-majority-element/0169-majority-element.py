class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        maj_ele, count = nums[0], 1

        for x in range(1, len(nums)):
            if nums[x] != maj_ele:
                count -= 1
                if count == 0:
                    maj_ele = nums[x]
                    count = 1
            else:
                count += 1

        return maj_ele


        