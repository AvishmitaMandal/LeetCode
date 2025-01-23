class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        n_row, n_col = len(matrix), len(matrix[0])
        self.prefix_sum = [[0] * (n_col+1) for _ in range(n_row+1)]

        # # prefix sum alomg col
        # curr_sum = self.prefix_sum[0][0]
        # for x in range(n_col):
        #     curr_sum += matrix[0][x]
        #     self.prefix_sum[0][x] = curr_sum

        # # prefix sum along row
        # curr_sum = self.prefix_sum[0][0]
        # for y in range(n_row):
        #     curr_sum += matrix[y][0]
        #     self.prefix_sum[y][0] = curr_sum

        # rest
        for y in range(1, n_row+1):
            for x in range(1, n_col+1):
                self.prefix_sum[y][x] = matrix[y-1][x-1] + self.prefix_sum[y-1][x] + self.prefix_sum[y][x-1] - self.prefix_sum[y-1][x-1]

        print(self.prefix_sum)

        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.prefix_sum[row2+1][col2+1] - self.prefix_sum[row1][col2+1] - self.prefix_sum[row2+1][col1] + self.prefix_sum[row1][col1]
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)