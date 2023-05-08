class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        heap = []
        N = len(heights)
        
        for i in range(N-1):
            diff = heights[i+1] - heights[i]
            
            if diff > 0:
                heapq.heappush(heap, diff)
            
            if len(heap) > ladders:
                bricks -= heapq.heappop(heap)
            if bricks < 0:
                return i
            
        return N - 1
            