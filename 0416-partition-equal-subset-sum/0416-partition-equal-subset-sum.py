class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        
        if sum(nums) % 2 != 0:
            return False
        
        target = sum(nums)//2
        memo = defaultdict(int)
        
        def dp(target, i):
            if i == len(nums):
                return False
            
            if target == 0:
                return True
            
            if (target, i) not in memo:
                memo[(target, i)] = dp(target - nums[i], i + 1) or dp(target, i + 1)
            
            return memo[(target, i)]
        
        return dp(target, 0) 