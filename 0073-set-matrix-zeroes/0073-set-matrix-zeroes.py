class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        
        zeros = []
        rows, cols = len(matrix), len(matrix[0])
        for row in range(rows):
            for col in range(cols):
                if matrix[row][col] == 0:
                    zeros.append((row, col))
        for rw,cl in zeros:  
            for row in range(rows):
                matrix[row][cl] = 0
            for col in range(cols):
                matrix[rw][col] = 0
        return matrix
        
        
"""
    Do not return anything, modify matrix in-place instead.
"""