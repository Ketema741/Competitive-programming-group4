class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
       # Check rows
        for row in board:
            seen = set()
            for num in row:
                if num != '.' and num in seen:
                    return False
                seen.add(num)

        # Check columns
        for i in range(len(board)):
            seen = set()
            for row in board:
                num = row[i]
                if num != '.' and num in seen:
                    return False
                seen.add(num)


        # Check 3x3 boxes
        for i in range(3):
            for j in range(3):
                seen = set()
                for m in range(3):
                    for n in range(3):
                        num = board[i*3+m][j*3+n]
                        if num != '.' and num in seen:
                            return False
                        seen.add(num)
        return True      