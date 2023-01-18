class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]: 
        rows, cols = len(grid), len(grid[0])  # Get the number of rows and columns
        res = [] 
        
        # Iterate through each element of the input grid
        for row in range(rows):
            row_maxs = [] 
            for col in range(cols):
                # Initialize a variable to store the maximum value within the 3x3 sub-grid
                max_ = -1
                
                # Determine the maximum value within the 3x3 sub-grid centered at the current element
                for sub_row in range(row, row + 3):
                    # Check if the sub-grid is within the bounds of the input grid
                    if (row + 3) > rows or (col + 3) > cols:
                        break
                    for sub_col in range(col, col + 3):
                        max_ = max(max_, grid[sub_row][sub_col])
                        
                # If a maximum value was found, append it to the list of maximum values for the current row
                if max_ != -1:
                    row_maxs.append(max_)
            # If there are any maximum values for the current row, append the row to the final output list
            if len(row_maxs):
                res.append(row_maxs)
        return res