class UnionFind:
    def __init__(self, size):
        self.parent = [i for i in range(size)]
        self.rank = [0] * size
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union_set(self, x, y):
        xset = self.find(x)
        yset = self.find(y)
        if xset == yset:
            return
        elif self.rank[xset] < self.rank[yset]:
            self.parent[xset] = yset
        elif self.rank[xset] > self.rank[yset]:
            self.parent[yset] = xset
        else:
            self.parent[yset] = xset
            self.rank[xset] += 1

class Solution:
    def minScore(self, n, roads):
        dsu = UnionFind(n + 1)
        answer = float('inf')

        for road in roads:
            dsu.union_set(road[0], road[1])

        for road in roads:
            if dsu.find(1) == dsu.find(road[1]):
                answer = min(answer, road[2])

        return answer
