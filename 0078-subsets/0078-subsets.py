class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
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