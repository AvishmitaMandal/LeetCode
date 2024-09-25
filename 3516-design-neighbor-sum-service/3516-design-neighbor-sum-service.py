class NeighborSum:

    def __init__(self, grid: List[List[int]]):
        self.n = len(grid)
        self.m = len(grid[0])
        self.grid = grid

        self.map = {}
        for x in range(self.n):
            for y in range(self.m):
                self.map[grid[x][y]] = [x, y]

    def adjacentSum(self, value: int) -> int:
        coords = self.map[value]
        x, y = coords[0], coords[1]

        res = 0
        if x+1 < self.n:
            res += self.grid[x+1][y]
        if y+1 < self.m:
            res += self.grid[x][y+1]
        if x-1 >= 0:
            res += self.grid[x-1][y]
        if y-1 >= 0:
            res += self.grid[x][y-1]

        return res  
        

    def diagonalSum(self, value: int) -> int:
        coords = self.map[value]
        x, y = coords[0], coords[1]

        res = 0
        if x+1 < self.n and y+1 < self.m:
            res += self.grid[x+1][y+1]
        if y+1 < self.m and x-1 >= 0:
            res += self.grid[x-1][y+1]
        if x-1 >= 0 and y-1>=0:
            res += self.grid[x-1][y-1]
        if y-1 >= 0 and x+1 < self.n:
            res += self.grid[x+1][y-1]

        return res  
        


# Your NeighborSum object will be instantiated and called as such:
# obj = NeighborSum(grid)
# param_1 = obj.adjacentSum(value)
# param_2 = obj.diagonalSum(value)