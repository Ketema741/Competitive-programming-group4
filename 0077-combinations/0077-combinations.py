class Solution:
    def __init__(self):
        self.res = []
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        def backtrack(com, i):
            if len(com) == k:
                self.res.append(com)
                return

            for j in range(i, n + 1):
                backtrack(com + [j], j + 1)
                
        backtrack([], 1)
        return self.res