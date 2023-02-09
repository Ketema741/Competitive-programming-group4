class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res =  [[1]]
        
        for _ in range(numRows - 1):
            upperRow = [0] + res[-1] + [0]
            lowerRow = []
            
            for indx in range(len(res[-1]) + 1):
                lowerRow.append(upperRow[indx] + upperRow[indx + 1])
                
            res.append(lowerRow)
            
        return res