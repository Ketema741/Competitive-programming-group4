class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        zeros_index = []
        rows, cols = len(matrix), len(matrix[0])
        
        # find row and col of zero 
        for row in range(rows):
            for col in range(cols):
                if matrix[row][col] == 0:
                    zeros_index.append((row, col))
                    
        #  change cols and rows to zero 
        for rw,cl in zeros_index:  
            for row in range(rows):
                matrix[row][cl] = 0
            for col in range(cols):
                matrix[rw][col] = 0
                
        return matrix
