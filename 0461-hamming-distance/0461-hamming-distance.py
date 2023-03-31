class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        count = 0
        while x or y:
            xDigit = x&1
            yDigit = y&1
            
            x, y = x>>1, y>>1
            
            count += yDigit ^ xDigit
            
        return count