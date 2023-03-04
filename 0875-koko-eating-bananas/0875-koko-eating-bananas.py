class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        def canEatAll(k, hrs_left):
            for pile in piles:
                hrs_left -= math.ceil(pile/k)
            return hrs_left >= 0

        l, r = 1, max(piles)
        while l < r:
            mid = (l+r)//2
            if canEatAll(mid, h):
                r = mid
            else:
                l = mid + 1
        return l