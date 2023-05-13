class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        heap = [-num for num in piles]
        heapq.heapify(heap)
        
        for _ in range(k):
            n = -heapq.heappop(heap) 
            heapq.heappush(heap, -(n -  n//2))
            k -= 1
            
        return -sum(heap)
