n, m = list(map(int, input().split()))
grid_len = 10**2 + 1

grid = [[0]*grid_len for _ in range(grid_len)]

for _ in range(n):
  x, y = list(map(int, input().split()))
  grid[x][y] += 1


for _ in range(m):
  x1, y1, x2, y2  = list(map(int, input().split())) 
  count = 0

  for row in range(x1, x2 + 1):
    for col in range(y1, y2 + 1):
      count += grid[row][col]
  print(count)
