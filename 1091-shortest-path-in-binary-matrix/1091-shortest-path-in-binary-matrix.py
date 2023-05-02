class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0], [1, 1], [-1, -1], [-1, 1], [1, -1]]
        visited = set((0,0))
        queue = deque([(0,0,1)])
        N = len(grid)
        
        if grid[0][0] or grid[N-1][N-1]:
            return -1
        
        def inbound(row, col):
            return  0 <= row < N and 0 <= col < N
        
        while queue:
            r, c, path_len = queue.popleft()
            
            if r == N - 1 and c == N - 1:
                return path_len
            
            for dr, dc in directions:
                row = r + dr
                col = c + dc
                
                if inbound(r, c) and (row, col) not in visited and grid[r][c] != 1:
                    queue.append((row, col, path_len + 1))
                    visited.add((row, col))
                    
        return -1