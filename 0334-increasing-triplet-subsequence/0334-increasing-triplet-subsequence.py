class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        MAX = 2**31
        first, second = MAX, MAX

        for num in nums:
            if num <= first:
                first = num
            elif num <= second:
                second = num
            else:
                return True

        return False
        