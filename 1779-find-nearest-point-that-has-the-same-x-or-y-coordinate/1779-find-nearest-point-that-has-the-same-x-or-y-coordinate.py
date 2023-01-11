class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        min_distance = float('inf')
        min_index = -1
        for i, point in enumerate(points):
            a, b = point
            if a == x or b == y:
                distance = abs(a - x) + abs(b - y)
                if distance < min_distance:
                    min_distance = distance
                    min_index = i
        return min_index
