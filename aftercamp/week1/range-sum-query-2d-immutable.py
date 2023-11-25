class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        row, col = len(matrix), len(matrix[0])
        self.p = [[0]*(col + 1) for _ in range(row + 1)]

        for r in range(1, row + 1):
            for c in range(1, col + 1):
                self.p[r][c] = self.p[r - 1][c] + self.p[r][c - 1] - self.p[r - 1][c - 1] + matrix[r - 1][c - 1]


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        res = self.p[row2 + 1][col2 + 1] - self.p[row1][col2 + 1] - self.p[row2 + 1][col1] + self.p[row1][col1]
        return res


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)