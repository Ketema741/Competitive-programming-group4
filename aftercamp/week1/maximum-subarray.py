class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        runing_sum = 0
        max_sum = -float(inf)
        
        for right in range(len(nums)):
            runing_sum += nums[right]
            
            if runing_sum < nums[right]:
                runing_sum = nums[right]
                
            max_sum = max(max_sum, runing_sum)
            
        return max_sum
        