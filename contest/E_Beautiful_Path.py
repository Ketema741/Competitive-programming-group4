

def replace(row, col, value):
    for col1 in range(col+1, cols):
        if grid[row][col1] == '*' or grid[row][col1] == 'T':
            break
        else:
            grid[row][col1] = value

    for col2 in range(col-1, -1, -1):
        if grid[row][col2] == '*':
            break
        else:
            grid[row][col2] = value

    for row1 in range(row+1, rows):
        if grid[row1][col] == '*' or grid[row1][col] == 'T':
            break
        else:
            grid[row1][col] = value

    for row2 in range(row-1, -1, -1):
        if grid[row2][col] == '*' or grid[row2][col] == 'T':
            break
        else:
            grid[row2][col] = value


rows, cols = map(int, input().split())
grid = []
for i in range(rows):
    temp, str_input = [], input()
    for char in str_input:
        temp.append(char)
    grid.append(temp)

for row in range(rows):
    for col in range(cols):
        if grid[row][col] == 'S':
            replace(row, col, 'S')

        if grid[row][col] == 'T':
            replace(row, col, 'T')


for row in range(rows):
    start = 'S'
    end = ''
    for col in range(cols):
        if start != grid[row][col]:
            start = grid[row][col]
        if grid[row][col] == 'T':
            end = 'T'
