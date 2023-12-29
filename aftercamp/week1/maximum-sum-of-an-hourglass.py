class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        res = 0
        
        for i in range(row - 2):
            for j in range(col - 2):
                sum_ = 0
                
                for k in range(j, j + 3):
                    # top horizontal items
                    sum_ += grid[i][k]
                    
                    # bottom horizontal items
                    sum_ += grid[i + 2][k]

                # middle items
                sum_ += grid[i + 1][j + 1]
                
                res = max(res, sum_)
                
        return res