class Solution:
    def calculateSum(self, nums, divisor):
        total = 0
        for num in nums:
            total += ceil(num/divisor)

        return total

    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        low, high = 1, max(nums)
        ans = 10**8

        while low <= high:
            mid = (low + high)//2

            total = self.calculateSum(nums, mid)
            if total <= threshold:
                ans = min(ans, mid)
                high = mid - 1
            else:
                low = mid + 1

        return ans


        