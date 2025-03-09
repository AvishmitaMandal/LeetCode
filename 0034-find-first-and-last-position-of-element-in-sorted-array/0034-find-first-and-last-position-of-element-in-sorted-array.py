class Solution:
    def findFirstOccurance(self, nums, target):
        ans = -1
        low, high = 0, len(nums)-1

        while low <= high:
            mid = (low + high)//2
            if nums[mid] == target:
                ans = mid
                high = mid - 1
            elif nums[mid] > target:
                high = mid - 1
            else:
                low = mid + 1

        return ans

    def findLastOccurance(self, nums, target):
        ans = -1
        low, high = 0, len(nums)-1

        while low <= high:
            mid = (low + high)//2
            if nums[mid] == target:
                ans = mid
                low = mid + 1
            elif nums[mid] > target:
                high = mid - 1
            else:
                low = mid + 1

        return ans

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        first = self.findFirstOccurance(nums, target)
        last = self.findLastOccurance(nums, target)

        return [first, last]
        