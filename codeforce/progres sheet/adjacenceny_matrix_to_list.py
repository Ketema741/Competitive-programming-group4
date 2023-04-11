from collections import defaultdict


n = int(input())
grid = []

for _ in range(n):
    row = list(map(int, (input().split())))
    grid.append(row)

matrix = defaultdict(list)

for row in range(n):
    for col in range(n):
        if grid[row][col]:
            matrix[row+1].append(col + 1)

for key, val in matrix.items():
    print(len(val), *val)
