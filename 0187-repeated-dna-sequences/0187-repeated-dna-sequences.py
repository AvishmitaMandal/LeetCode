from collections import defaultdict
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        mp = defaultdict(int)
        res = set()

        if len(s) < 10:
            return list(res)

        start, end = 0, 9

        while end < len(s): 
            substr = s[start:end+1]
            
            if substr in mp:
                res.add(substr)

            mp[substr] += 1
            end += 1
            start += 1

        return list(res)

        