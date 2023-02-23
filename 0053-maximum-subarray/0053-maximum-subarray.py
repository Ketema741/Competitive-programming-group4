class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sum_ = 0
        max_sum = -float(inf)
        
        for right in range(len(nums)):
            sum_ += nums[right]
            
            if sum_ < nums[right]:
                sum_ = nums[right]
                
            max_sum = max(max_sum, sum_)
            
        return max_sum
        