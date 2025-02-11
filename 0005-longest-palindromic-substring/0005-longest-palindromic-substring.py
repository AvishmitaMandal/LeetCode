class Solution:

    def longestPalindrome(self, s: str) -> str:
        '''
        s = "babad"
        abcbbaaaaaaaabbcba
        '''

        max_len = 0
        ptr = 0
        res = ""

        for ptr in range(len(s)):
            start, end = ptr, ptr
            homogenous = 1
            while start >=0 and end < len(s):
                substr_len = end - start + 1
                if substr_len > max_len:
                    max_len = max(max_len, substr_len)
                    res = s[start:end+1]

                if start-1 >= 0 and end+1 < len(s) and s[start-1]==s[end+1]: 
                    if s[start]!= s[start-1]:
                        homogenous = 0
                    start -= 1
                    end += 1
                elif start-1 >=0 and homogenous and s[start] == s[start-1]:
                    start -= 1
                elif end+1 < len(s) and homogenous and s[end] == s[end+1]:
                    end += 1
                else:
                    break

        return res
                




        