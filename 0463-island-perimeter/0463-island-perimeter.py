class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
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
            count = 0
            if not inbound(row, col) or grid[row][col] == 0:
                return 1
                
            if visited[row][col]:
                return 0
            
            visited[row][col] = True
            
            for row_change, col_change in directions:
                new_row = row + row_change
                new_col = col + col_change
                
                count += dfs(grid, visited, new_row, new_col)
                        
            return count
  
        start_row, start_col = startingPoint(grid)
        
        return dfs(grid, visited, start_row, start_col)                    