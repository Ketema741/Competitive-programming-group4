class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        path = set()
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        def inbound(row, col):
            return (0 <= row < ROWS and 0 <= col < COLS)

        def dfs(r, c, i):
            if i == len(word):
                return True
            
            if not inbound(r, c) or (r, c) in path:
                return False
            
            path.add((r, c))
            
            if board[r][c] == word[i]:
                for rw, cl in directions:
                    if dfs(r + rw, c + cl, i + 1):
                        return True

            path.remove((r, c))
            return False
        

        # To prevent TLE,reverse the word if frequency of the first letter is more than the last letter's
        count = defaultdict(int, sum(map(Counter, board), Counter()))
        if count[word[0]] > count[word[-1]]:
            word = word[::-1]
            
        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0):
                    return True
                
        return False

    # O(n * m * 4^n)
