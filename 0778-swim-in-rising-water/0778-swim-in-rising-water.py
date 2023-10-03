class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        visited = set()
        row = col = len(grid)
        directions = [ (0, -1),(0, 1), (-1, 0), (1, 0)]
            
        
        def inbound(r, c):
            return 0 <= r < row and 0 <= c < col
        
        res = float("inf")
        
        minHeap = [(grid[0][0], 0, 0)]
        
        while minHeap:
            elevation, r1, c1  = heapq.heappop(minHeap)
                    
            if (r1, c1) in visited:
                continue
                    
            if r1 == c1 == row - 1:
                    return elevation
                    
            visited.add((r1, c1))
            
            for r2, c2 in directions:
                newR, newC = r1 + r2, c1 + c2
                
                if inbound(newR, newC):
                    
                    if elevation < grid[newR][newC]:
                        heapq.heappush(minHeap, (grid[newR][newC], newR, newC))
                    else:
                        heapq.heappush(minHeap, (elevation, newR, newC))
            
        
        