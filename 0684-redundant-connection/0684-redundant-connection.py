class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [1] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        parent_of_x, parent_of_y = self.find(x), self.find(y)

        if parent_of_x != parent_of_y:
            if self.rank[parent_of_x] >= self.rank[parent_of_y]:
                self.parent[parent_of_y] = parent_of_x
                self.rank[parent_of_x] += self.rank[parent_of_y]
            elif self.rank[parent_of_x] < self.rank[parent_of_y]:
                self.parent[parent_of_x] = parent_of_y
                self.rank[parent_of_y] += self.rank[parent_of_x]

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        res = []
        union_find = UnionFind(len(edges))
        for a, b in edges:
            a -= 1
            b -= 1
            
            if union_find.find(a) == union_find.find(b):
                res.append([a+1, b+1])
                
            union_find.union(a, b)
        
        return res[-1]
        
        
        