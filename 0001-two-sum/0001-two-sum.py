class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        hash_sum = {}
        for x in range(len(nums)):
            if nums[x] in hash_sum:
                hash_sum[nums[x]].append(x)
            else:
                hash_sum[nums[x]] = [x]

        res = []

        for key, val in hash_sum.items():
            if (target-key) in hash_sum:
                if key == target-key:
                    if len(hash_sum[key]) > 1:
                        return hash_sum[key]
                else:
                    res.append(hash_sum[key][0])
                    res.append(hash_sum[target-key][0])
                    return res

        return res

        