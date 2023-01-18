class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]: 
        rows, cols = len(grid), len(grid[0])
        res = []
        
        for row in range(rows):
            row_maxs = [] 
            for col in range(cols):
                max_ = -1
                
                # determine max value with in 3 X 3 grid
                for sub_row in range(row, row + 3):
                    if (row + 3) > rows or (col + 3) > cols:
                        break
                    for sub_col in range(col, col + 3):
                        max_ = max(max_, grid[sub_row][sub_col])
                        
                if max_ != -1:
                    row_maxs.append(max_)
            if len(row_maxs):
                res.append(row_maxs)
        return res
