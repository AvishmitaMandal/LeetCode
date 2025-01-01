class Solution:
    def crossMultiplication(self, prev, curr):
        res = []
        for p in prev:
            for c in curr:
                st = p+c
                res.append(st)

        return res

    def letterCombinations(self, digits: str) -> List[str]:
        
        result = []
        n = len(digits)
        if n == 0:
            return result

        digitmap = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }

        prev = digitmap[digits[0]]
        if n == 1:
            return prev

        for x in range(1, len(digits)):
            curr = digitmap[digits[x]]
            result = self.crossMultiplication(prev, curr)
            prev = result

        return result


        