class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        res = 0
        
        if k > numOnes:
            res += numOnes
            k -= numOnes
            if k  > 0:
                k -= numZeros
            if k > 0:
                res -= k
            return res
        else:
            return k
                
            