class Solution:
    def findMin(self, nums: List[int]) -> int:
        DUMMY_MAX = 5001
        ans = DUMMY_MAX

        low, high = 0, len(nums)-1
        while low <= high:
            mid = (low + high)//2
            if nums[low] <= nums[mid]:
                ans = min(ans, nums[low])
                low = mid + 1
            elif nums[mid] <= nums[high]:
                ans = min(ans, nums[mid])
                high = mid - 1

        return ans
