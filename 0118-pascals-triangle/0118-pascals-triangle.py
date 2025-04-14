class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = []
        n = numRows

        level1 = [1]
        res.append(level1)
        if n == 1:
            return res

        level2 = [1,1]
        res.append(level2)
        if n == 2:
            return res

        prev_level = level2
        for x in range(3, n+1):
            curr_level = [1]
            for y in range(1, len(prev_level)):
                curr_level.append(prev_level[y-1] + prev_level[y])
            curr_level.append(1)
            res.append(curr_level)
            prev_level = curr_level

        return res

            

        