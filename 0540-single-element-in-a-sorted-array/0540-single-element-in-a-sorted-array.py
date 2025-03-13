class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        low, high = 0, len(nums)-1

        if len(nums) == 1:
            return nums[0]

        while low <= high:
            mid = (low + high)//2

            # success condition
            if mid == 0:
                if nums[mid]!= nums[mid+1]:
                    return nums[mid]
            elif mid == len(nums)-1:
                if nums[mid] != nums[mid-1]:
                    return nums[mid]
            elif nums[mid-1] != nums[mid] and nums[mid] != nums[mid+1]:
                return nums[mid]

            # failure condition
            if nums[mid] == nums[mid-1]:
                if mid % 2 == 0:
                    high = mid-2
                else:
                    low = mid+1
            else:
                if mid % 2 !=0:
                    high = mid-1
                else:
                    low = mid + 2

        return 
                

        