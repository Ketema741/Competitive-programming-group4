class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        def canEatAll(k, hrs_left):
            for pile in piles:
                hrs_left -= math.ceil(pile/k)
            
            return hrs_left >= 0

        left, right = 1, max(piles)
        
        while left <= right:
            mid = left + (right - left) // 2
            
            if canEatAll(mid, h):
                right = mid - 1
            else:
                left = mid + 1
                
        return left
        