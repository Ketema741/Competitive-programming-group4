class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        cols = len(grid[0])
        row1 = grid[0].copy()
        row2 = grid[1].copy()

        for i in range(1, cols):
            row1[i] += row1[i - 1]
            row2[i] += row2[i - 1]
        

        res = float("inf")

        for i in range(cols):
            top = row1[-1] - row1[i]
            bottom = row2[i - 1] if i > 0 else 0
            second_robot = max(top, bottom)

            res = min(res, second_robot)

        return res