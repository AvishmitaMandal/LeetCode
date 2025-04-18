class Solution:
    def permuteRecurse(self, nums, visited, temp, res):
        if len(nums) == len(temp):
            res.append(temp.copy())
            return res

        for x in range(len(nums)):
            if nums[x] not in visited:
                temp.append(nums[x])
                visited.add(nums[x])
                res = self.permuteRecurse(nums, visited, temp, res)
                visited.remove(nums[x])
                temp.pop()

        return res


    def permute(self, nums: List[int]) -> List[List[int]]:
        visited = set()
        res = []
        temp = []
        res = self.permuteRecurse(nums, visited, temp, res)
        return res
        