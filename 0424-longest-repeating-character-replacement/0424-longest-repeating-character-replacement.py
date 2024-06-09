class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if len(s) == 0:
            return 0
        
        freq_dict = {}

        start, end = 0, 0
        most_freq = 0

        res = 0

        while end < len(s):
            if s[end] in freq_dict:
                freq_dict[s[end]] += 1
            else:
                freq_dict[s[end]] = 1

            most_freq = max(most_freq, freq_dict[s[end]])

            rep_freq = (end - start + 1) - most_freq
            
            if rep_freq > k:
                freq_dict[s[start]] -= 1
                start += 1
            else:
                res = max(res, end - start + 1)

            end += 1

        return res


        