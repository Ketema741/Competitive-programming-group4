class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)
        
        prefix_mult = 1
        for indx, num in enumerate(nums):
            res[indx] = prefix_mult
            prefix_mult *= num
        
        suffix_mult = 1
        for indx in range(len(nums) - 1, -1, -1):
            res[indx] *= suffix_mult 
            suffix_mult *= nums[indx]
            
        return res