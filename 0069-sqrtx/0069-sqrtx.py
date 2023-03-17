class Solution:
    def mySqrt(self, x: int) -> int:
        left, right = 0, x//2
        
        while left <= right:
            mid = left + (right - left)//2
            
            if mid**2 > x:
                right = mid - 1
            else:
                left = mid + 1
                
        return left if left**2 <= x else left - 1