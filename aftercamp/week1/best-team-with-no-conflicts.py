class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        pairs = [[scores[i], ages[i]] for i in range(len(ages))]
        pairs.sort()

        dp = [pairs[i][0] for i in range(len(ages))]

        for i in range(1, len(ages)):
            for j in range(i):
                if pairs[i][1] >= pairs[j][1]:
                    dp[i] = max(dp[i], pairs[i][0] + dp[j])
                    
        
        return max(dp)