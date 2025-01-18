import heapq

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        '''
            ABCAAABCAABAC, k = 3
        '''
        if len(s) == 0:
            return 0

        start, end = 0, 0
        maxLength = 1
        hashmap = {}
        highFreqChar, highFreqVal = '', 0

        while end < len(s):
            if s[end] not in hashmap or hashmap[s[end]] == 0:
                hashmap[s[end]] = 1
            else:
                hashmap[s[end]] += 1

            if hashmap[s[end]] > highFreqVal:
                highFreqChar = s[end]
                highFreqVal = hashmap[s[end]]
                
            length = end-start+1
            if length - highFreqVal <= k:
                maxLength = max(maxLength, length)
            else:
                hashmap[s[start]] -= 1
                start += 1

            end += 1

        return maxLength

            

        

