class Solution:
    def arrangeCoins(self, n: int) -> int:
        res = 0
        left, right = 0, n
        
        while left <= right:
            mid = left + (right - left)//2
            
            if self.canBuild(mid, n):
                left = mid + 1
            else:
                right = mid - 1
                
        return right

    def canBuild(self, coins, n):
            return coins*(coins + 1)/2 <= n
            
            