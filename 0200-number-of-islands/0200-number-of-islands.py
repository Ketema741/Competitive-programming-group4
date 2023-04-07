class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        visited = set()
        islands = 0
        
        def inbound(row, col):
            return  0 <= row < len(grid) and 0<= col < len(grid[0])
        
        def dfs(row, col):
            
            if not inbound(row, col) or grid[row][col] == "0" or (row, col) in visited:
                return 
            
            visited.add((row, col))
            
            for row_change, col_change in directions:
                dfs(row + row_change, col + col_change)
        
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if (row, col) not in visited and grid[row][col] == "1":
                    islands += 1
                    dfs(row, col)
                    
        return islands