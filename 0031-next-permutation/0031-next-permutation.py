class Solution:
    def swap(self, nums, i, j):
        temp = nums[i]
        nums[i] = nums[j]
        nums[j] = temp

        return

    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if n == 1:
            return nums
            
        if nums[n-1] > nums[n-2]:
            self.swap(nums, n-1, n-2)
        else:
            x = n-1
            while x >= 0 and nums[x] <= nums[x-1]:
                x -= 1
            
            # reverse
            i, j = x, n-1
            while i <= j:
                self.swap(nums, i, j)
                i += 1
                j -= 1

            for y in range(x, n):
                if nums[x-1] < nums[y]:
                    self.swap(nums, x-1, y)
                    break
            
        return nums
        