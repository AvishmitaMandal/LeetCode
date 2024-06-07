class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 2:
            return len(s)
        
        start, end, max_len = 0,0,0
        d = {}

        while end < len(s):

            # No duplicates in the substring
            if s[end] not in d or d[s[end]]==0:
                d[s[end]] = 1

            # Duplicate found
            else:
                while s[start] != s[end]:
                    d[s[start]] = 0
                    start+=1
                d[s[start]] = 0
                start += 1
                d[s[end]] = 1

            max_len = max(max_len, end-start+ 1)
            end += 1

        return max_len

        