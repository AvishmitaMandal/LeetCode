class Solution:
    def swap(self, x, y, matrix):
        temp = matrix[x][y]
        matrix[x][y] = matrix[y][x]
        matrix[y][x] = temp

    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        
        # Transpose in place
        for x in range(m):
            for y in range(x+1,m):
                self.swap(x,y,matrix)

        # Reverse
        for x in range(m):
            matrix[x] = reversed(matrix[x])


        