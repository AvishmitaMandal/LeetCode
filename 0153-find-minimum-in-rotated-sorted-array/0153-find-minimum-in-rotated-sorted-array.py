class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        start, end = 0, n-1

        while start <= end:
            mid = (start + end) // 2

            if mid > 0 and mid < n-1 and nums[mid] < nums[mid-1] and nums[mid] < nums[mid + 1]:
                return nums[mid]

            if nums[mid] > nums[end]:
                start = mid + 1
            elif nums[start] > nums[mid]:
                end = mid -1
            else:
                return nums[start]

        return nums[0]

        