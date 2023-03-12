class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtrack(indx, curnt_subset):
            res.append(curnt_subset[:])
            
            for i in range (indx, n):
                curnt_subset.append(nums[i])
                backtrack(i+1, curnt_subset)
                curnt_subset.pop()
        
        res, n = [], len(nums)
        backtrack(0, [])
        
            
        return res