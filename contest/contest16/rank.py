from ast import List


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
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int):
        union_find = UnionFind(n)

        for a, b in edges:
            union_find.union(a, b)

        return union_find.find(source) == union_find.find(destination)