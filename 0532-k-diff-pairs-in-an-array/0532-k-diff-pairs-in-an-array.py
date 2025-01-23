from collections import defaultdict
class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        hashmap = defaultdict(int)

        pair_set = set()

        for num in nums:
            if num - k in hashmap:
                pair_set.add((num-k,num))
            if num + k in hashmap:
                pair_set.add((num, num+k))

            hashmap[num] = 1

        return len(pair_set)


        