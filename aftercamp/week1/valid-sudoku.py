class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows, cols = len(board), len(board[0])
        hash_map = defaultdict(list)
        for row in range(rows):
            for col in range(cols):
                if board[row][col] != '.':
                    hash_map[(row, 'r')].append(board[row][col])
                    hash_map[(col, 'c')].append(board[row][col])
                    
        for values in hash_map.values():
            if len(values) != len(set(values)):
                return False


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