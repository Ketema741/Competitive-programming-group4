class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        def backtrack(start, comb):
            if len(comb) == k:
                res.append(comb.copy())
                return
            
            if start > n or len(comb) > k:
                return
            
            # inclue nums at i
            comb.append(start)
            backtrack(start + 1, comb ) #  then explore
            
            # not include nums at i
            comb.pop()
            backtrack(start + 1, comb) #  then explore

        backtrack(1, [])
        return res
    
    
    """
    subset question solution:
        def backtrack(indx, subset):
            if indx >= len(nums):
                res.append(subset.copy())
                return
            
            # include nums[i]
            subset.append(nums[indx])      
            backtrack(indx+1, subset)       # explore
            
            # not include nums[i]
            subset.pop()                   
            backtrack(indx+1, subset)       # explore
    """
    
    
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
