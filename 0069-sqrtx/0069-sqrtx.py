class Solution:
    def mySqrt(self, x: int) -> int:
        low, high = 0, x//2
        mid = (low + high)//2
        
        while low <= high:
            mid = (low + high) // 2
            
            if mid**2 > x:
                high = mid - 1
            else:
                low = mid + 1
                
        return low if low**2 <= x else low-1