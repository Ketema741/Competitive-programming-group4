class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])
        res = 0
        
        for i in range(R - 2):
            
            for j in range(C - 2):
                sum_ = 0
                
                # top horizontal items
                for k in range(j, j + 3):
                    sum_ += grid[i][k]

                # middle items
                sum_ += grid[i + 1][j + 1]
                
                # bottom horizontal items
                for k in range(j, j + 3):
                    sum_ += grid[i + 2][k]
                
                res = max(res, sum_)
                
        return res