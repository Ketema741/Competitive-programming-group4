class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        left, right = 0, len(x) - 1
        
        while right > left:
            if x[left] != x[right]:
                return False
            left += 1
            right -= 1
        return True
        
        
        
        """
               l
            0  1  2    
            1  2  1
               r
        """