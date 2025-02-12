class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []

        mp = {
            '2' : ['a', 'b', 'c'],
            '3' : ['d', 'e', 'f'],
            '4' : ['g', 'h', 'i'],
            '5' : ['j', 'k', 'l'],
            '6' : ['m', 'n', 'o'],
            '7' : ['p', 'q', 'r', 's'],
            '8' : ['t', 'u', 'v'],
            '9' : ['w', 'x', 'y', 'z']
        }

        res = []

        for c in digits:
            c_map = mp[c]
            new_res = []
            if len(res) == 0:
                new_res = c_map
            else:
                for char in c_map:
                    for r in res:
                        new_res.append(r+char)

            res = new_res
        
        return res