pos = [(-1, -2), (-1, 2), (1, -2), (1, 2), (-2, 1), (-2, -1), (2, 1), (2, -1)]

def isInvalid(r, c):
    if r >= 4 or c >= 3 or r < 0 or c < 0:
        return True
    if (r, c) in [(3, 0), (3, 2)]:
        return True
    return False

class Solution:
    def knightDialer(self, n: int) -> int:
        cache = {}
        mod = 1000000007
        def dfs(row, col, moves):
            if isInvalid(row, col):
                return 0
            
            if n == moves:
                return 1
            
            if (row, col, moves) in cache:
                return cache[(row, col, moves)]
            
            dials = 0
            for r0, c0 in pos:
                dials += dfs(row + r0, col + c0, moves + 1)
                
            cache[(row, col, moves)] = dials
            return cache[(row, col, moves)] % mod

        res = 0
        for row in range(4):
            for col in range(3):
                res += dfs(row, col, 1)
                
        return res % mod