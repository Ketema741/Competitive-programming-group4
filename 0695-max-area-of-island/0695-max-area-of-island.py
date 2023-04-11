class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        visited = set()
        res = 0
        
        def inbound(row, col):
            return  0 <= row < len(grid) and 0<= col < len(grid[0])
        
        def dfs(row, col):
            count = 1
            visited.add((row, col))
            
            for r, c in directions:
                new_row, new_col = row + r, col + c
                
                if inbound(new_row, new_col) and grid[new_row][new_col] == 1 and (new_row, new_col) not in visited:
                    count += dfs(row + r, col + c)
                
            return count
        
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if (row, col) not in visited and grid[row][col] == 1:
                    res = max(res, dfs(row, col))
                    
        return res