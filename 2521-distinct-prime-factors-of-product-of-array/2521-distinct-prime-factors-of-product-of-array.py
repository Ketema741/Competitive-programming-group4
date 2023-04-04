class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        factors = set()
        
        def factor(num):
            i = 2

            while num and i < num:
                if num%i == 0:
                    factors.add(i)
                    num = num//i
                else:
                    i += 1
            if num:
                factors.add(num)
                    
        for num in nums:
            factor(num)
            
        return len(factors)  
