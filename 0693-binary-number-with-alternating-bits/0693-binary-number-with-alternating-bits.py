class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        
        first = n&1
        while n:
            n = n>>1
            second = n&1
            if second != first:
                first = second
            else:
                return False
            
        return True