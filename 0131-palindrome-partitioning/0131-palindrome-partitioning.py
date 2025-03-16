class Solution:
    def isPallindrome(self, s):
        if s == s[::-1]:
            return True
        return False

    def solve(self, s, ptr, parts, res):
        if ptr == len(s):
            # print(parts)
            res.append(parts.copy())
            return res

        for x in range(ptr, len(s)):
            if self.isPallindrome(s[ptr:x+1]):
                parts.append(s[ptr:x+1])
                res = self.solve(s, x+1, parts, res)
                parts.pop()

        return res

    def partition(self, s: str) -> List[List[str]]:
        res = []
        parts = []

        ptr = 0
        res = self.solve(s, ptr, parts, res)

        return res
        