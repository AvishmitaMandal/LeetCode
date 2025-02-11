from collections import defaultdict
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        '''
        abcabcbb
        tmmzuxt
        '''
        n = len(s)
        if n == 0:
            return 0

        start, end = 0,0
        mp = defaultdict(int)

        res = 0
        while end < n:
            if s[end] in mp and mp[s[end]] != 0:
                while s[start] != s[end]:
                    mp[s[start]] -= 1
                    start += 1
                mp[s[start]] -= 1
                start += 1

            res = max(res, end-start+1)
            mp[s[end]] += 1
            end += 1

        return res

        