class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        
        res = [[0 for _ in range(n)] for _ in range(n)]
        
        for querie in queries:
            row1, col1, row2, col2 =  querie
            

            for row in range(row1, row2 + 1):
                res[row][col1] += 1
            
            for row in range(row1, row2 + 1):
                if col2+1 < n:
                    res[row][col2 + 1] -= 1
        
        for row in range(n):
            
            for col in range(1, n):
                res[row][col] = res[row][col] + res[row][col - 1]
                    
        return res