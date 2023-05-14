class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        count = defaultdict()
        
        for word in words:
            count[word] = 1 + count.get(word, 0)
            
        heap = []
        
        for key, val in count.items():
            heapq.heappush(heap, (-val, key))
            
        res = []
        for _ in range(k):
            _, key = heapq.heappop(heap)
            res.append(key)
        
        return res