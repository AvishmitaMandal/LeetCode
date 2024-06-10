class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        dict_map = {}

        for num in nums:
            if num in dict_map:
                dict_map[num] += 1
            else:
                dict_map[num] = 1
        
        zeroes, ones, twos = 0,0,0
        
        if 0 in dict_map:
            zeroes = dict_map[0]
        if 1 in dict_map:
            ones = dict_map[1]
        if 2 in dict_map:
            twos = dict_map[2]

        x = 0
        while zeroes != 0:
            nums[x] = 0
            x += 1
            zeroes -= 1

        while ones != 0:
            nums[x] = 1
            x += 1
            ones -= 1

        while twos != 0:
            nums[x] = 2
            x += 1
            twos -= 1


        