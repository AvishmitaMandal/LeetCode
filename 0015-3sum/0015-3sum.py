class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        res = []

        for i in range(n):
            if i!=0 and nums[i] == nums[i-1]:
                continue
            j, k = i+1, n-1
            while j < k:
                total = nums[i] + nums[j] + nums[k]
                if total == 0:
                    res.append([nums[i], nums[j], nums[k]])
                    while j+1 < n and nums[j+1] == nums[j]:
                        j += 1
                    while k-1 >= 0 and nums[k-1] == nums[k]:
                        k -= 1
                    k -= 1
                elif total > 0:
                    k -= 1
                else:
                    j += 1

        return res