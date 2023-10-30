class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:        
        dp = {}
        
        def dfs(a, b, stones):
            if len(stones) == 0:
                return abs(a - b)
            
            entry = (a, b, len(stones)) 

            if entry in dp:
                return dp[entry]
            
            num = stones.pop()
            m = min(dfs(a + num, b, stones), dfs(a, b + num, stones))
            stones.append(num)
            
            dp[entry] = m 
            
            return dp[entry]
        
        return dfs(0, 0, stones)