class Solution:
    def divideByFour(self, num):
            if num == 1:
                return True

            if num < 1:
                return False

            val = num / 4

            return self.divideByFour(val)
        
        
    def isPowerOfFour(self, n: int) -> bool:
        res = self.divideByFour(n)
        return res
    