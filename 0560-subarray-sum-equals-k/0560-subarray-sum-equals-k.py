from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        mp = defaultdict(int)
        prefix_sum = [0]

        total = 0
        for x in range(n):
            total += nums[x]
            prefix_sum.append(total)

        print(prefix_sum)

        count = 0
        for x in range(len(prefix_sum)):
            if prefix_sum[x]-k in mp:
                count += mp[prefix_sum[x]-k]
            mp[prefix_sum[x]] += 1

        return count

        

        


        