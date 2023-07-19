class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        
        memo = defaultdict(int)
        
        def dp(n):
            
            if n >= len(nums):
                return 0
            
            if n in memo:
                return memo[n]
            
            money = max(nums[n] + dp(n+2), dp(n+1))
            memo[n] = money
            
            return memo[n]
        
        return dp(0)