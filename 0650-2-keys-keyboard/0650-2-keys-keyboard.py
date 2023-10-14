class Solution:
    def minSteps(self, n: int) -> int:
        if n == 1:
            return 0
        if n == 2:
            return 2
        dp = [float('inf')] * (n+1)  
        dp[1] = 0
        dp[2] = 2
        
        for i in range(3, n + 1):
            for j in range(1, i):
                if (i - j) % j == 0:
                    dp[i] = min(dp[i], dp[j] + 1 + (i-j)//j)

        return dp[n]