class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        res, heap = [], []

        for key, val in freq.items():
            heapq.heappush(heap, (val, key))

            if len(heap) > k:
               heapq.heappop(heap)
        
        while heap:
            res.append(heapq.heappop(heap)[1])

        return res
