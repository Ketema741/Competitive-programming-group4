class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        pairs = [(num1, num2) for num1, num2 in zip(nums1, nums2)]

        pairs = sorted(pairs, key=lambda p:p[1], reverse=True)

        minHeap = []
        n1Sum = 0
        res = 0

        for n1, n2 in pairs:
            n1Sum += n1
            heapq.heappush(minHeap, n1)

            if len(minHeap) > k:
                num1 = heapq.heappop(minHeap)
                n1Sum -= num1

            if len(minHeap) == k:
                res = max(res, n1Sum * n2)
        
        return res
