class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_hash = {}
        prefix_sum = 0

        for x in range(len(nums)):
            prefix_sum += nums[x]
            if prefix_sum not in prefix_hash:
                prefix_hash[prefix_sum] = [x]
            else:
                prefix_hash[prefix_sum].append(x)

        res = 0
        if k in prefix_hash:
            res += len(prefix_hash[k])

        for key, val in prefix_hash.items():
            if (key + k) in prefix_hash:
                for i in prefix_hash[key]:
                    for j in prefix_hash[key+k]:
                        if i < j:
                            res += 1

        return res

        

        