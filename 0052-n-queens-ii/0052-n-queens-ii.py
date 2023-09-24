class Solution:
    def totalNQueens(self, n: int) -> int:
        col = set()
        negDiag = set()
        posDiag = set()
        
        board = [["."] * n for _ in range(n)]
        res = 0
        
        def backtrack(r):
            nonlocal res
            if r == n:
                res += 1
            for c in range(n):
                if c in col or r + c in posDiag or r - c in negDiag:
                    continue
                
                board[r][c] = "Q"
                col.add(c)
                negDiag.add(r - c)
                posDiag.add(r + c)
                
                backtrack(r + 1)
                
                board[r][c] = "."
                col.remove(c)
                negDiag.remove(r - c)
                posDiag.remove(r + c)
                
        backtrack(0)
        return res
        