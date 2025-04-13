class Solution:
    # def swap(self, x, y, matrix):
    #     temp = matrix[x][y]
    #     matrix[x][y] = matrix[y][x]
    #     matrix[y][x] = temp

    #     return matrix

    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        #  Symmetric inversion
        n = len(matrix)
        for x in range(n):
            for y in range(x+1, n):
                temp = matrix[x][y]
                matrix[x][y] = matrix[y][x]
                matrix[y][x] = temp
                print(matrix)

        #  Reverse each row
        for x in range(n):
            matrix[x].reverse()

        return matrix
        

        
