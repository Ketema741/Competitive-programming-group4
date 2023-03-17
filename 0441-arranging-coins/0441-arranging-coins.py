class Solution:
    def arrangeCoins(self, n: int) -> int:
        res = 0
        
        left, right = 0, n
        
        while left <= right:
            
            mid = left + (right - left)//2
            
            coins = mid*(mid + 1)/2
            
            if coins <= n:
                res = max(res, mid)
                left = mid + 1
            else:
                right = mid - 1
                
        return res
            
            