class UnionFind:
    def __init__(self, n):
        self.leaders = [i for i in range(n)]
        self.ranks = [1 for i in range(n)]
    
    def find(self, x):
        if self.leaders[x] != x:
            self.leaders[x] = self.find(self.leaders[x])
        return self.leaders[x]

    def union(self, x, y):
        p = self.find(x)
        q = self.find(y)
        if p == q: 
            return False
        if self.ranks[p] < self.ranks[q]:
            self.leaders[p] = q
        elif self.ranks[p] > self.ranks[q]:
            self.leaders[q] = p
        else:        
            self.leaders[q] = p
            self.ranks[p] += 1
        return True
    
class Solution:
    def hasValidPath(self, grid):
        m, n = len(grid), len(grid[0])
        right = {1: {1, 3, 5}, 2: {}, 3: {}, 4: {1, 3, 5}, 5: {}, 6: {1, 3, 5}}
        down = {1: {}, 2: {2, 5, 6}, 3: {2, 5, 6}, 4: {2, 5, 6}, 5: {}, 6: {}}
        uf = UnionFind(m * n)
        for x in range(m):
            for y in range(n):
                if y + 1 <= n - 1 and grid[x][y + 1] in right[grid[x][y]]:
                    uf.union(x * n + y, x * n + y + 1)
                if x + 1 <= m - 1 and grid[x + 1][y] in down[grid[x][y]]:
                    uf.union(x * n + y, (x + 1) * n + y)
        return uf.find(0) == uf.find(m * n - 1)