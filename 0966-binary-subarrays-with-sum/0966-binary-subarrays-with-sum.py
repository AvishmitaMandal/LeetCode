from collections import defaultdict
class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        hashmap = defaultdict(int)
        hashmap[0] = 1
        count = 0

        curr_sum = 0
        for num in nums:
            curr_sum += num

            if curr_sum - goal in hashmap:
                count += hashmap[curr_sum-goal]
            
            hashmap[curr_sum] += 1

        return count
        