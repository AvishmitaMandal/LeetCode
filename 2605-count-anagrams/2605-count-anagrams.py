from collections import defaultdict
import math

class Solution:
    def countAnagrams(self, s: str) -> int:
        '''
        "too hot for me"
        '''
        MOD = 10**9 + 7

        i = 0
        res = 1
        while i < len(s):
            hashmap = defaultdict(int)
            word_len = 0
            while i < len(s) and s[i]!= ' ':
                hashmap[s[i]]+= 1
                word_len += 1
                i += 1

            res *= math.factorial(word_len)
            for key, val in hashmap.items():
                res *= pow(math.factorial(val), MOD-2, MOD)
            i += 1

        return res % MOD
            

        