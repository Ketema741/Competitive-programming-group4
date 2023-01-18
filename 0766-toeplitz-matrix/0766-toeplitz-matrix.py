class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        # Get the number of rows and columns
        rows, cols = len(matrix), len(matrix[0])  
        
        # Iterate through each element of the input matrix
        for row in range(rows):
             for col in range(cols):
                    sub_col = col
                    sub_row = row
                    while  sub_row + 1 < rows and sub_col +1 < cols:
                        if matrix[sub_row + 1][sub_col + 1] != matrix[row][col]:
                            return False
                        sub_row += 1
                        sub_col += 1
        return True