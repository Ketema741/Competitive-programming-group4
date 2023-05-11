class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)

        heap = []

        for key, value in freq.items():
            heapq.heappush(heap, (value, key))

            if len(heap) > k:
                heapq.heappop(heap)

        result = []
        while heap:
            result.append(heapq.heappop(heap)[1])

        return result[::-1]