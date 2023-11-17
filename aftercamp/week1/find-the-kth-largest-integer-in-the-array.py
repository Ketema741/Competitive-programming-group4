class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        minHeap = [int(num) for num in nums]
        heapq.heapify(minHeap)

        while len(minHeap) > k:
            heapq.heappop(minHeap)
        
        return str(minHeap[0])

"""
    COMPLEXITY
    Time: O(nlogn) Sorting
    Space: O(n) to change str to int
"""