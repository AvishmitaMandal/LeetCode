class Solution:
    def swap(self, i, j, nums):
        temp = nums[i]
        nums[i] = nums[j]
        nums[j] = temp 

        return nums

    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        low, mid, high = 0, 0, n-1

        while mid <= high:
            if nums[mid] == 0:
                nums = self.swap(low, mid, nums)
                low += 1
                mid += 1
            elif nums[mid] == 1:
                mid += 1
            elif nums[mid] == 2:
                nums = self.swap(mid, high, nums)
                high -= 1
            

        