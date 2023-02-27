class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = prefixSum = 0
        res = len(nums)
        
        if sum(nums) < target:
            return 0
        
        for right in range(len(nums)):
            prefixSum += nums[right]
            
            while prefixSum >= target:
                res = min(res, right - left + 1)
                prefixSum -= nums[left]  
                left += 1
                
        return res