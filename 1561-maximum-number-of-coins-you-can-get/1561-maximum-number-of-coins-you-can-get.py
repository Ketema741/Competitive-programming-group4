class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        if len(piles) < 3:
            return 0
        
        piles.sort()
        left, right = 0, len(piles) - 2
        sum_  = 0
        
        while left < right:
            sum_ += piles[right]
            left += 1
            right -= 2
        
        return sum_