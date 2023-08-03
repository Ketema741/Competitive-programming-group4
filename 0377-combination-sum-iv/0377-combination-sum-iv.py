class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        memo = {}
        
        def dp(target):
            if target == 0:
                return 1
            
            if target not in memo:
                total = 0
                
                for num in nums:
                    if target - num >= 0:
                        total += dp(target - num)
                
                memo[target] = total
                
            return memo[target]
        
        return dp(target)
            
            