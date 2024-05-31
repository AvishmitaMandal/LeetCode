class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        MAX = 2**31

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    matrix[i][j] = MAX

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == MAX:
                    for m in range(len(matrix)):
                        if matrix[m][j] != MAX:
                            matrix[m][j] = 0
                    
                    for n in range(len(matrix[0])):
                        if matrix[i][n] != MAX:
                            matrix[i][n] = 0

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == MAX:
                    matrix[i][j] = 0
        