class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        for rows in range(len(matrix)):
            
            if matrix[rows][-1] < target:
                continue
            for cols in range(len(matrix[0])):
                if matrix[rows][cols] == target:
                    return True
        return False