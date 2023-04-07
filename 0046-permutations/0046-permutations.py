class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        def permutation(temp, nums):
            if len(nums) == 0:
                res.append(temp[:])
                return
            
            
            for i in range(len(nums)):
                permutation(temp + [nums[i]], nums[:i] + nums[i+1:]) #explore
                    
        permutation([], nums)
        
        return res