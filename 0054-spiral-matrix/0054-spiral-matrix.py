class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:  return []
        rows, cols = len(matrix), len(matrix[0])
        res = []
        left, right = 0, cols - 1
        top, bottom = 0, rows - 1
        
        while left <= right and top <= bottom:
            for indx in range(left, right + 1):
                res.append(matrix[top][indx])
            top += 1
            
            for indx in range(top, bottom + 1):
                res.append(matrix[indx][right])
            right -= 1
            
            if top <= bottom:
                for indx in range(right, left - 1, -1):
                    res.append(matrix[bottom][indx])
                bottom -= 1
            
            if left <= right:
                for indx in range(bottom, top - 1, -1):
                    res.append(matrix[indx][left])
                left += 1
                
        return res