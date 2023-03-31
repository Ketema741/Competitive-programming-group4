class Solution:
    def findGCD(self, nums: List[int]) -> int:
        num1, num2 = min(nums), max(nums)
        
        def gcd(a, b):
            if b == 0:
                return a
            return gcd(b, a % b)
        
        return gcd(num1, num2)