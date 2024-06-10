class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # s1_dict = {}
        # s1_len = len(s1)

        # for c in s1:
        #     if c in s1_dict:
        #         s1_dict[c] += 1
        #     else :
        #         s1_dict[c] = 1

        # x = 0
        # while x < len(s2):
        #     if s2[x] in s1_dict:
        #         dict_copy = s1_dict.copy()
        #         k = 0
        #         while k < s1_len:
        #             if x+k < len(s2) and s2[x+k] in dict_copy and dict_copy[s2[x+k]]>0:
        #                 dict_copy[s2[x+k]] -= 1
        #                 k += 1
        #             else:
        #                 break
        #         if k == len(s1):
        #             return True

        #     x += 1

        # return False

        s1_sorted = sorted(s1)
        n = len(s1)
        m = len(s2)

        for x in range(m-n+1):
            potential_perm = sorted(s2[x:x+n])
            if s1_sorted == potential_perm:
                return True

        return False


        
        