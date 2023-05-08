class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        if not matrix or not matrix[0]:
            return -1
        
        heap = []
        
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                num = -matrix[row][col]
                
                if len(heap) < k:
                    heapq.heappush(heap, num)
                elif num > heap[0]:
                    heapq.heappushpop(heap, num)
                    
        return -heap[0]