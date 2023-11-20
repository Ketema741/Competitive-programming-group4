class Solution(object):
    def kClosest(self, points, k):
        res = []

        for i, coord in enumerate(points):
            x, y = coord
            points[i] = (x**2 + y**2, [x, y])

        heapq.heapify(points)

        while len(res) < k:
            distance, coord = heapq.heappop(points)
            res.append(coord)

        return res