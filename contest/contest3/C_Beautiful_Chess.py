N = int(input())
res = []
rows = cols = 8

for _ in range(N):
    grid = []  
    input() # empty line
    
    # take grid values
    for _ in range(rows):
        grid_row = []
        grid.append(input())

    # determine row and column of bishop
    for row in range(1, rows-1):
        for col in range(1, cols-1):
            if grid[row][col] == '#':
                if grid[row - 1][col - 1] == '#' and grid[row + 1][col + 1] == '#':
                    if grid[row - 1][col + 1] == '#' and grid[row + 1][col - 1] == '#':
                        res.append((row + 1, col + 1))
                        break
                    
# print row, col, of bishop for each test case
for pair in res:
    print(pair[0], pair[1])