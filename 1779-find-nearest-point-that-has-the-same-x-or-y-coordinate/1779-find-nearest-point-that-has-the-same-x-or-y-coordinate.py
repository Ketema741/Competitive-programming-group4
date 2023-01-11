class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        min_distance = float('inf')
        min_index = -1
        for indx, (x2, y2) in enumerate(points):
            if x2 == x or y2 == y:
                distance = abs(x2 - x) + abs(y2 - y)
                if distance < min_distance:
                    min_distance = distance
                    min_index = indx
        return min_index