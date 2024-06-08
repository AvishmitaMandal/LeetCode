class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        prev_list = [1]
        k = 1

        while k <= rowIndex:
            new_list = []
            new_list.append(1)
            for x in range(1,k):
                new_list.append(prev_list[x-1]+prev_list[x])
            new_list.append(1)
            prev_list = new_list.copy()
            k += 1

        return prev_list
        