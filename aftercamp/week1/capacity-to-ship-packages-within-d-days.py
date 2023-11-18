class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left, right = max(weights), sum(weights)
        res = right
        
        def canShip(cap):
            ships, curCap = 1, cap
            
            for weight in weights:
                if curCap - weight < 0:
                    ships += 1
                    curCap = cap
                
                curCap -= weight
                
            return ships <= days
        
        while left <= right:
            cap = left + (right - left)//2
            
            if canShip(cap):
                right = cap - 1
                res = min(res, cap)
            else:
                left = cap + 1
                
        return res