class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        # Get the number of rows and columns
        rows, cols = len(matrix), len(matrix[0])  
        
        # Iterate through each element of the input matrix
        for row in range(rows):
            for col in range(cols):
                # variables to keep track of the current sub-matrix
                sub_col = col
                sub_row = row
                # check diagonally if current sub-matrix is still within the bounds
                while  sub_row + 1 < rows and sub_col + 1 < cols:
                
                    # compare the value of the current sub-matrix with the value of the starting element
                    if matrix[sub_row + 1][sub_col + 1] != matrix[row][col]:
                        # If not, return False as the input matrix is not a Toeplitz matrix
                        return False
                    # Move to the next sub-matrix
                    sub_row += 1
                    sub_col += 1
        # If all sub-matrices have been checked and none have returned false,  matrix is a Toeplitz 
        return True