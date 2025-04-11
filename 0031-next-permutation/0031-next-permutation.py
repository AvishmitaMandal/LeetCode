class Solution:
    def swap(self, i, j, nums):
        temp = nums[i]
        nums[i] = nums[j]
        nums[j] = temp

    def reverse(self, nums, idx):
        start, end = idx, len(nums)-1
        while start < end:
            self.swap(start, end, nums)
            start += 1
            end -= 1

        return nums

    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        pivot_idx = -1
        for x in range(n-1, 0, -1):
            if nums[x-1] < nums[x]:
                pivot_idx = x
                break

        if pivot_idx == -1:
            nums.reverse()
            return nums

        else:
            nums = self.reverse(nums, pivot_idx)
            temp_min = float("inf")
            temp_min_index = -1
            for x in range(pivot_idx, n):
                if nums[x] > nums[pivot_idx-1]:
                    if nums[x] < temp_min:
                        temp_min = nums[x]
                        temp_min_index = x
            self.swap(temp_min_index, pivot_idx-1, nums)

        return nums






        