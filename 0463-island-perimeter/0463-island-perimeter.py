class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        count = 0
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        visited = [[0 for i in range(len(grid[0]))] for j in range(len(grid))]
        
        def inbound(row, col):
            return (0 <= row < len(grid) and 0 <= col < len(grid[0]))
        
        def startingPoint(grid):
            for row in range(len(grid)):
                for col in range(len(grid[0])):
                    if grid[row][col]:
                        return (row, col)
        
        def dfs(grid, visited, row, col):
            nonlocal count
            
            visited[row][col] = True
            
           
            for row_change, col_change in directions:
                new_row = row + row_change
                new_col = col + col_change
                
                if inbound(new_row, new_col):
                    if not visited[new_row][new_col] and  grid[new_row][new_col] == 1:
                        dfs(grid, visited, new_row, new_col)
                        
                if not inbound(new_row, new_col) or grid[new_row][new_col] == 0:
                    count += 1
        
        start_row, start_col = startingPoint(grid)
        
        dfs(grid, visited, start_row, start_col)
        
        return count
                    