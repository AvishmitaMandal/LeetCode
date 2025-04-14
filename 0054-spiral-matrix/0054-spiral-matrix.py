class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])

        left, right = 0, n-1
        top, bottom = 0, m-1

        res = []

        while top <= bottom and left <= right:
            # right
            for x in range(left, right+1):
                res.append(matrix[top][x])

            top += 1
            # down
            for x in range(top, bottom+1):
                res.append(matrix[x][right])

            right -= 1
            # left
            if top <= bottom:
                for x in range(right, left-1, -1):
                    res.append(matrix[bottom][x])

            bottom -= 1
            if left <= right:
                for x in range(bottom, top-1, -1):
                    res.append(matrix[x][left])

            left += 1

        return res

        