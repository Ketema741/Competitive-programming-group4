class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        def backtrack(indx, subset):
            if indx >= len(nums):
                res.append(subset.copy())
                return
            
            subset.append(nums[indx])       # choose
            backtrack(indx+1, subset)       # explore
            subset.pop()                    # unchoose
            backtrack(indx+1, subset)       # explore
                
        backtrack(0, [])
        
        return res