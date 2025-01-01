class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = []

        # Brute force way
        # [2,7,11,15] - O(n^2) time and O(1) space 

        # Maps
        # [2,7,11,15]

        hashMap = {}
        for x in range(len(nums)):
            if nums[x] not in hashMap:
                hashMap[nums[x]] = []
            hashMap[nums[x]].append(x)
        print(hashMap)

        for key, val in hashMap.items():
            if (target - key) in hashMap:
                if target - key != key:
                    res.append(val[0])
                    res.append(hashMap[target-key][0])
                    return res
                else:
                    if len(hashMap[target-key]) > 1:
                        res.append(hashMap[target-key][0])
                        res.append(hashMap[target-key][1])
                        return res

        return 0

        


        