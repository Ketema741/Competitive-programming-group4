class Solution(object):
    def kClosest(self, points, k):
        maxHeap = []
        res = []

        for x, y in points:
            distance = x**2 + y**2
            heapq.heappush(maxHeap, (distance, [x, y]))

        while len(res) < k:
            distance, coord = heapq.heappop(maxHeap)
            res.append(coord)

        return res
        