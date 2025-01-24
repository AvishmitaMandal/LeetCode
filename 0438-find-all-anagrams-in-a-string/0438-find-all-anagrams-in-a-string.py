class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        '''
        p = "abc"
        [1, 1, 1, 0....]

        [0,1,1,0,1....] -> 0
        '''
        p_count_freq = [0] * 26
        s_count_freq = [0] * 26

        for c in p:
            p_count_freq[ord(c)-ord('a')] += 1

        start, end = 0, 0
        res = []

        while end < len(s):
            s_count_freq[ord(s[end])-ord('a')] += 1
            end += 1

            if end - start > len(p):
                s_count_freq[ord(s[start])-ord('a')] -= 1
                start += 1

            if end - start == len(p) and s_count_freq == p_count_freq:
                res.append(start)

        return res

                
        