class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        def backtrack(indx, subset):
            if indx == len(nums):
                res.append(subset[:])
                return
            
            res.append(subset[:])
            
            for i in range(indx, len(nums)):
                subset.append(nums[i])      # choose
                backtrack(i+1, subset)      # explore
                subset.pop()                # unchoose
                
        backtrack(0, [])
        
        return res