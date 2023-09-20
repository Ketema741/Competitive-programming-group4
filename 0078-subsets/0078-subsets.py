class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
       # bit manipulation total num of subset = 2^n
    
        res = []
        n = len(nums)
        for i in range(2**n):
            subset = []
            
            for j in range(n):
                # check each bit weather it set(1) or not(0)
                if (i>>j) & 1:
                    subset.append(nums[j])
            res.append(subset)
            
        return res
                
        
    
    
    
    
    
    
    
    
    
    
    """
     res = []
        
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
                
        backtrack(0, [])
        
        return res
    """