class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        start, end = 0, 0
        maxScore = 0
        totalSum = 0
        hashmap = {}

        while end < len(nums):
            if nums[end] in hashmap and hashmap[nums[end]] != 0:
                while start < end and nums[start] != nums[end]:
                    totalSum -= nums[start]
                    hashmap[nums[start]] -= 1
                    start += 1
                totalSum -= nums[start]
                hashmap[nums[start]] -= 1
                start += 1

            if nums[end] not in hashmap:
                hashmap[nums[end]] = 1
            else:
                hashmap[nums[end]] += 1
            totalSum += nums[end]
            maxScore = max(totalSum, maxScore)
            end += 1

        return maxScore

        