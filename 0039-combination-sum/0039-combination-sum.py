class Solution:
    def combinationSumBacktrack(self, total, candidates, res, target, temp, curr):
        if total > target:
            return
        if total == target:
            temp.sort()
            res.append(temp.copy())
            return

        for x in range(curr,len(candidates)):
            c = candidates[x]
            total += c
            temp.append(c)
            self.combinationSumBacktrack(total, candidates, res, target, temp, x)
            temp.pop()
            total -= c

        return

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        total = 0
        temp = []
        candidates.sort()
        self.combinationSumBacktrack(total, candidates, res, target, temp, 0)
        return res
        
        