class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        res = []
        
        for row in range(len(matrix[0])):
            res.extend(matrix[row])
        res.sort()
        
        return res[k - 1]