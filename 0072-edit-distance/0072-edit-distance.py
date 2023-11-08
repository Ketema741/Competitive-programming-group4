class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n1, n2 = len(word1), len(word2)
        cache = [[float("inf")]*(n2 + 1) for _ in range(n1 + 1)]

        for i in range(n1 + 1):
            cache[i][n2] = n1 - i

        for i in range(n2 + 1):
            cache[n1][i] = n2 - i

        for i in range(n1-1, -1, -1):
            for j in range(n2 - 1, -1, -1):
                if word1[i] == word2[j]:
                    cache[i][j] = cache[i + 1][j + 1]
                else:
                    cache[i][j] = 1 + min(cache[i+1][j], cache[i][j+1], cache[i+1][j+1])
    
        return cache[0][0]