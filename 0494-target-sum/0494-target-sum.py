class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = defaultdict(int)
        n = len(nums)

        def dp(index, rem):
            key = (index, rem)

            if index < 0:
                return 1 if rem == 0 else 0

            if key not in memo:
                plus = dp(index - 1, rem + nums[index])
                minus = dp(index - 1, rem - nums[index])
                
                memo[key] = plus + minus
           
            return memo[key]
            
        return dp(n - 1, target)

