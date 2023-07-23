class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        hash_map = defaultdict(int)
        n = len(cost)
        
        def dp(n):
            if n < 2:
                return cost[n]
            
            if n not in hash_map:
                hash_map[n] = cost[n] + min(dp(n - 1), dp(n - 2))
                
            return hash_map[n]
        
        return min(dp(n-1), dp(n-2))