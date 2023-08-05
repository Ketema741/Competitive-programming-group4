class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        res = tot = nums[0]
        
        for i in range(1, len(nums)):
            tot += nums[i]
            res = max(res, math.ceil(tot/(i+1)))
            
        return res