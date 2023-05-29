from typing import List
from collections import defaultdict

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = defaultdict(int)

        def dp(i):
            if i >= len(cost):
                return 0

            if memo[i] != 0:
                return memo[i]

            memo[i] = cost[i] + min(dp(i+1), dp(i+2))

            return memo[i]

        return min(dp(0), dp(1))
