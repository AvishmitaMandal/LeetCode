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
        fact_hashmap = defaultdict(int)

        while i < len(s):
            hashmap = defaultdict(int)
            word_len = 0
            while i < len(s) and s[i]!= ' ':
                hashmap[s[i]]+= 1
                word_len += 1
                i += 1

            if word_len not in fact_hashmap:
                fact_hashmap[word_len] = math.factorial(word_len)
                
            res *= fact_hashmap[word_len] % MOD

            for key, val in hashmap.items():
                if val not in fact_hashmap:
                    fact_hashmap[val] = math.factorial(val)
                res *= pow(fact_hashmap[val], MOD-2, MOD)
            i += 1

        return res % MOD
            

        