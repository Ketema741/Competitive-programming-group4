class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        memo = [0 for _ in range(len(triangle) + 1)] 
        
        for row in triangle[::-1]:
            for i, num in enumerate(row):
                memo[i] = num + min(memo[i], memo[i+1])
                
        return memo[0]