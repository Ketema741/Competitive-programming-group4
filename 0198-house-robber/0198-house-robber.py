class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = defaultdict(int)
        
        def dp(n):
            
            if n == 0:
                return nums[n]
            
            if n == 1:
                return max(nums[0], nums[1])
            
            if n not in memo:
                memo[n] = max(dp(n - 1), dp(n - 2) + nums[n])
            
            return memo[n]
        
        return dp(len(nums) - 1)