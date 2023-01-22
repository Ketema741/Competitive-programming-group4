# extra space
def rotate_grid(grid):
    n = len(grid)
    m = len(grid[0])
    rotated_grid = [[0]*m for i in range(n)]
    for i in range(n):
        for j in range(m):
            rotated_grid[j][n-1-i] = grid[i][j]
    return rotated_grid




# in place
def rotate_grid_inplace(grid):
    n = len(grid)
    # Transpose the matrix
    for i in range(n):
        for j in range(i, n):
            grid[i][j], grid[j][i] = grid[j][i], grid[i][j]
    # Reverse each row
    for i in range(n):
        grid[i] = grid[i][::-1]
    return grid


