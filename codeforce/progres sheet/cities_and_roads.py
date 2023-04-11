from collections import defaultdict


n = int(input())
grid = []

for _ in range(n):
    row = list(map(int, (input().split())))
    grid.append(row)

res = 0
for row in range(n):
    res += sum(grid[row])
print(res//2)            