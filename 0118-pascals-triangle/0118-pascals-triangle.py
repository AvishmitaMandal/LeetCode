class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = []
        if numRows == 0:
            return res

        prev_list = [1]
        res.append(prev_list)

        k = 2
        while k <= numRows:
            new_list = []
            new_list.append(1)
            for x in range(1,k-1):
                new_list.append(prev_list[x-1]+prev_list[x])
            new_list.append(1)
            res.append(new_list)
            prev_list = new_list.copy()
            k+=1

        return res
        