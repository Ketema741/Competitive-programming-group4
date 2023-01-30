class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        R, C = len(matrix), len(matrix[0])
        res = [[None] * R for _ in range(C)]
        
        for r, row in enumerate(matrix):
            for c, val in enumerate(row):
                res[c][r] = val
                
        return res