from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        '''
        ["eat","tea","tan","ate","nat","bat"]
        Approach 1 :
        aet - eat, tea, ate
        atn - tan, nat
        abt - bat
        TC : O(mnlogm)
        SC : O(n)
        '''

        hashmap = defaultdict(list)
        for s in strs:
            sorted_str = ''.join(sorted(s))
            hashmap[sorted_str].append(s)

        res = []

        for key, val in hashmap.items():
            res.append(val)

        return res

        