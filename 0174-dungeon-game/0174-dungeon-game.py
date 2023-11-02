class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        row, col = len(dungeon), len(dungeon[0])
        dp = [[0]*col for _ in range(row)]
        dp[row - 1][col - 1] = max(1 - dungeon[row - 1][col - 1], 1)

        for i in range(row - 2, -1, -1):
            dp[i][col - 1] = max(dp[i + 1][col - 1] - dungeon[i][col - 1], 1)

        for i in range(col - 2, -1, -1):
            dp[row - 1][i] = max(dp[row - 1][i + 1] - dungeon[row - 1][i], 1)

        for i in range(row - 2, -1, -1):
            for j in range(col - 2, -1, -1):
                min_health_on_exit = min(dp[i][j+1], dp[i + 1][j])

                dp[i][j] = max(min_health_on_exit - dungeon[i][j], 1)

        return dp[0][0]