class Solution:
    # method for swapping 2 numbers
    def swap(self, nums, first, second):
        temp = nums[first]
        nums[first] = nums[second]
        nums[second] = temp

    def nextPermutation(self, nums: List[int]) -> None:
        # len = 1
        if len(nums) == 1:
            return nums

        # asc case
        n = len(nums)
        if nums[n-1] > nums[n-2]:
            self.swap(nums, n-1, n-2)
            print(nums)

        # desc case - non-increasing
        else:
            left = n-2
            right = n-1

            while nums[left] >= nums[right]:
                if left == 0:
                    left = -1
                    break
                left -= 1
                right -= 1
            left += 1
            print(left)

            start, end = left, n-1
            while start < end:
                self.swap(nums, start, end)
                start += 1
                end -= 1
            print(nums)
            # exists a pivot element
            if left != 0:
                p = left - 1
                x = p + 1
                while x < n and nums[x] <= nums[p]:
                    x += 1
                self.swap(nums, x, p)





            
