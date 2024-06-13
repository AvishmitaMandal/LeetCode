class Solution:
    def find_min(self, nums):
        n = len(nums)
        start, end = 0, n-1

        while start <= end:
            mid = (start+end) // 2

            if mid > 0 and mid < n-1 and nums[mid-1] > nums[mid] and nums[mid] < nums[mid + 1]:
                return mid

            if nums[start] > nums[mid]:
                end = mid-1
            elif nums[mid] > nums[end]:
                start = mid+1
            else:
                return start

        return 0        

    def find_bs(self, nums, target, start, end):

        while start <= end:
            mid = (start + end) // 2

            if nums[mid] == target:
                return mid

            if nums[mid] > target:
                end = mid-1
            else:
                start = mid + 1

        return -1

    
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        pivot_index = self.find_min(nums)
        # print(pivot_index)

        if pivot_index == 0:
            return self.find_bs(nums,target,0,n-1)

        start1, end1, start2, end2 = 0, pivot_index-1, pivot_index, n-1

        if nums[start1] <= target and target <= nums[end1]:
            return self.find_bs(nums, target, start1, end1) 
        
        
        return self.find_bs(nums, target, start2, end2)
        