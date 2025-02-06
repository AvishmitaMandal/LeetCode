class Solution:
    def bs_first(self, nums, target):
        low, high = 0, len(nums)-1
        ans = -1

        while low <= high:
            mid = (low + high) // 2

            if nums[mid] >= target:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1

        if nums[ans] != target:
            return -1
        return ans

    def bs_last(self, nums, target):
        low, high = 0, len(nums)-1
        ans = -1

        while low <= high:
            mid = (low + high) // 2

            if nums[mid] <= target:
                ans = mid
                low = mid + 1
            else:
                high = mid - 1

        if nums[ans] != target:
            return -1
        return ans

    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()

        first = self.bs_first(nums, target)
        last = self.bs_last(nums, target)

        if first == -1 or last == -1:
            return []

        res = []
        for x in range(first, last+1):
            res.append(x)

        return res
        