class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        
        
        def helper(n, k):
            if n == 1 :
                return 0
            if k%2 == 0:
                return 1 - helper(n-1, math.ceil(k/2))
            else:
                return helper(n-1, math.ceil(k/2))
        
        return helper(n, k)