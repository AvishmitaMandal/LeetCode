class Solution:
    def bs_lte(self, nums, target):
        low, high = 0, len(nums)-1
        ans = -1

        while low <= high:
            mid = (low+high)//2
            if nums[mid] >= target:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1

        if nums[ans]!= target:
            return -1

        return ans

    def bs_gte(self, nums, target):
        low, high = 0, len(nums)-1
        ans = -1

        while low <= high:
            mid = (low + high)//2
            if nums[mid] <= target:
                ans = mid
                low = mid + 1
            else:
                high = mid - 1
    
        if nums[ans]!= target:
            return -1
        return ans


    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0:
            return [-1,-1]
        
        start = self.bs_lte(nums, target)
        end = self.bs_gte(nums, target)

        if start == -1 or end == -1:
            return [-1, -1]

        res = [start, end]
        return res