class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zeroes, ones, twos = 0, 0, 0
        for num in nums:
            if num == 0:
                zeroes += 1
            if num == 1:
                ones += 1
            if num == 2:
                twos += 1

        x = 0
        while zeroes:
            nums[x] = 0
            zeroes -= 1
            x += 1
    
        while ones:
            nums[x] = 1
            ones -= 1
            x += 1

        while twos:
            nums[x] = 2
            twos -= 1
            x += 1
        