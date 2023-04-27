
from typing import List
from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque([])
        fresh = 0
        time_elapsed = 0
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        
        def is_inbound(row, col):
            return 0 <= row < ROWS and 0 <= col < COLS
    
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 1:
                    fresh += 1
                    
                if grid[row][col]  == 2:
                    queue.append((row, col))
                    
        while fresh > 0 and queue:
            for i in range(len(queue)):
                r, c = queue.popleft()
                
                for r_change, c_change in directions:
                    row = r + r_change
                    col = c + c_change
                    
                    if is_inbound(row, col) and grid[row][col] == 1:
                        grid[row][col] = 2
                        queue.append((row, col))
                        fresh -= 1
                        
            time_elapsed += 1
                
        return time_elapsed if fresh == 0 else -1