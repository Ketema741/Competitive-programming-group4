class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        
        left, right = 1, num//2
        if num == 1:
            return True
        while left <= right:
            mid = left + (right - left)//2
            
            sqr = mid**2
            if sqr == num:
                return True
            if sqr < num:
                left = mid + 1
            else:
                right = mid-1
                
        return False
        
        