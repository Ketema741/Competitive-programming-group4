class Solution:
    def countArrangement(self, N: int) -> int:
        count = 0
        visited = [False] * (N + 1)
        
        def backtrack(N, pos, visited):
            nonlocal count
            
            if pos > N:
                count += 1

            for i in range(1, N+1):
                if not visited[i] and (pos % i == 0 or i % pos == 0):
                    visited[i] = True # choose 
                    backtrack(N, pos+1, visited) # explore 
                    visited[i] = False # unchooose

        backtrack(N, 1, visited)
        
        return count