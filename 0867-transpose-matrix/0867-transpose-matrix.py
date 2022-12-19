class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        R, C = len(matrix), len(matrix[0])
        
        res = [[None] * R for _ in range(C)]
        for r, row in enumerate(matrix):
            for c, val in enumerate(row):
                res[c][r] = val
        return res


        """
         class Solution(object):
        def transpose(self, A):
            R, C = len(A), len(A[0])
            ans = [[None] * R for _ in xrange(C)]
            for r, row in enumerate(A):
                for c, val in enumerate(row):
                    ans[c][r] = val
            return ans

        #Alternative Solution:
        #return zip(*A)
        """