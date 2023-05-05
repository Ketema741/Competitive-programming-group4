n = int(input())

grid = []

for _ in range(n):
    row = list(map(int, (input().split())))
    grid.append(row)

source = []
sink = []
for row in range(n):
    if 1  not in grid[row]:
        sink.append(row+1)


for col in range(n):
    column = []
    for row in range(n):
        column.append(grid[row][col])

    if 1 not in column:
        source.append(col+1)  
        
source.sort()
sink.sort()          
print(len(source),*source)        
print(len(sink),*sink)        