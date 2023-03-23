class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        def backtrack(start, comb):
            if len(comb) == k:
                res.append(comb.copy())
                return
            
            if start > n:
                return
            
            comb.append(start) # choose
            backtrack(start + 1, comb ) #  then explore
            
            comb.pop() # unchoose
            backtrack(start + 1, comb) #  then explore

        backtrack(1, [])
        return res
    
    
    
    """
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        def backtrack(start, comb):
            if len(comb) == k:
                res.append(comb.copy())
                return
            
            for i in range(start, n+1):
                comb.append(i)
                backtrack(i+1, comb)
                comb.pop()
                
        backtrack(1, [])
        return res
    
    """
