class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        rows, cols = len(mat), len(mat[0])
        flat_list, _2D_list  = [], []
        
        if r * c != len(mat) * len(mat[0]):
            return mat #return original matrix if reshape is not possible.
        
        #Flatten the input matrix 
        for row in range(rows):
            for col in range(cols):
                flat_list.append(mat[row][col])
        
        # reshape to new dimensions specified by (r,c)
        for indx in range(r):
            _2D_list.append(flat_list[indx*c: ( (indx + 1)*c )])
            
        return _2D_list
