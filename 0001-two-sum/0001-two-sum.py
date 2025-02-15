class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mp = {}
        res = []

        for x in range(len(nums)):
            if target - nums[x] in mp:
                res.append(x)
                res.append(mp[target-nums[x]])
                return res
            mp[nums[x]] = x
            

        return res
        