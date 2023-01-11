class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        valid_indx = -1
        min_dist = math.inf
        
        for indx, (x2, y2) in enumerate(points):
            dist_x = x - x2
            dist_y = y - y2
            
            if dist_x * dist_y == 0 and abs(dist_x + dist_y) < min_dist:
                min_dist = abs(dist_x + dist_y)
                valid_indx = indx
                
        return valid_indx