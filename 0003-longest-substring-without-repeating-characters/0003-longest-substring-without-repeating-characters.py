class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        '''
        abcabcbb
        pwwkew
        '''
        if len(s) == 0:
            return 0
            
        max_length = 1
        start, end = 0, 0
        hash_map = {}
        hash_map[s[start]] = 1

        while end < len(s)-1:
            end += 1

            if s[end] not in hash_map or hash_map[s[end]] == 0:
                hash_map[s[end]] = 1
                length = end - start + 1
                if length > max_length:
                    max_length = length
            else :
                hash_map[s[end]] += 1
                while start <= end and s[start] != s[end]:
                    hash_map[s[start]] -= 1
                    start += 1
                hash_map[s[start]] -= 1
                start += 1

        return max_length
                    

            
        