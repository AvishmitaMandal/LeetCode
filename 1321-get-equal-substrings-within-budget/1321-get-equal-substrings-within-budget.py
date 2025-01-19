class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        nums = []
        for x in range(len(s)):
            nums.append(abs(ord(s[x])-ord(t[x])))

        maxLength = 0
        start, end = 0, 0
        totalSum = 0

        while end < len(nums):
            totalSum += nums[end]
            if totalSum > maxCost:
                while start <= end and totalSum > maxCost:
                    totalSum -= nums[start]
                    start += 1

            maxLength = max(maxLength, end-start+1)
            end += 1

        return maxLength
        