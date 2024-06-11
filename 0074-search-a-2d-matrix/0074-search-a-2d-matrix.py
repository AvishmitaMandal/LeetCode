class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n_rows = len(matrix)
        n_cols = len(matrix[0])

        start, end = 0, n_rows * n_cols - 1

        while start <= end:
            mid = (start+end) // 2

            col = mid // n_cols
            row = mid % n_cols

            if matrix[col][row] == target:
                return True

            elif matrix[col][row] < target:
                start = mid + 1

            else:
                end = mid - 1

        return False
        