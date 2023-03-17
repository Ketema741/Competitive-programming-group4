class NumMatrix:

    def __init__(self, matrix: List[List[int]]): 
       # horizontal prefixsum 
        for row in range(len(matrix)):
            for col in range(1, len(matrix[0])):
                matrix[row][col] += matrix[row][col - 1]
                   
       # vertical prefixsum
        p = 0
        while p < len(matrix[0]):
            for row in range(1, len(matrix)):
                matrix[row][p] += matrix[row - 1][p]
            p += 1
            
        self.matrix = matrix

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        answer = self.matrix[row2][col2]
        
        if col1 - 1 >= 0: 
            answer -= self.matrix[row2][col1 - 1]
            
        if row1 - 1 >= 0:
            answer -= self.matrix[row1 - 1][col2]
            
        if row1 - 1 >= 0 and col1 - 1 >= 0:
            answer += self.matrix[row1 - 1][col1 - 1]
            
        return answer