class Solution:
    def divideByThree(self, num):
        if num == 1:
            return True

        if num < 1:
            return False

        return self.divideByThree(num/3)
        
    def isPowerOfThree(self, n: int) -> bool:
        res = self.divideByThree(n)
        
        return res