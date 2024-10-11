class Solution:
    def rob(self, nums: List[int]) -> int:
        max_rob = []
        max_rob.append(0)
        max_rob.append(nums[0])

        for x in range(1, len(nums)):
            opt_rob = max(nums[x] + max_rob[x-1], max_rob[x])
            max_rob.append(opt_rob)

        return max_rob[len(max_rob)-1]
        