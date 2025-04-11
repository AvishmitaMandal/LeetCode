from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        '''
        "AABABBA", k = 1
        '''
        start, end = 0, 0
        mp = defaultdict(int)
        n = len(s)

        max_freq = 0
        res = 0

        while end < n:
            mp[s[end]] += 1
            if mp[s[end]] > max_freq:
                max_freq = mp[s[end]]
            size = end - start + 1

            operations_needed = size - max_freq
            if operations_needed <= k:
                res = max(res, size)
                end += 1
                continue
            else:
                mp[s[start]] -= 1
                start += 1

            end += 1

        return res
