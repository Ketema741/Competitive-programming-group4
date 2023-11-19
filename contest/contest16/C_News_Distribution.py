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
            

def distribution():
    n, m = list(map(int, input().split()))
    uf = UnionFind(n+1)
    for _ in range(m):
        groups = list(map(int, input().split()))

        if groups[0] >= 1:
            x = groups[1]
            for i in range(1, len(groups)):
                uf.union(x, groups[i])
    
    res = []

    for i in range(1, n+1):
        res.append(uf.rank[uf.find(i)])
    
    print(*res)
distribution()

