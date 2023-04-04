class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        count = 0
        while x or y:
            xLastDigit = x&1
            yLastDigit = y&1
            
            count += xLastDigit ^ yLastDigit
            
            x, y = x>>1, y>>1
            
        return count