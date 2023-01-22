class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        # Define chessboard dimensions
        rows, cols = 8, 8
        
        # King's position
        row, col = king
        
        # Store attacking queens
        res = []

        # Check for queens attacking from top
        for x in range(row, -1, -1):
            if [x, col] in queens:
                res.append([x, col])
                break

        # Check for queens attacking from bottom
        for x in range(row, rows):
            if [x, col] in queens:
                res.append([x, col])
                break
                
        # Check for queens attacking from left
        for y in range(col, -1, -1):
            if [row, y] in queens:
                res.append([row, y])
                break
        
        # Check for queens attacking from right
        for y in range(col, cols):
            if [row, y] in queens:
                res.append([row, y])
                break
            
        # Check for queens attacking from top-left diagonal
        for x, y in zip(range(row, -1, -1), range(col, -1, -1)):
            if [x, y] in queens:
                res.append([x, y])
                break
        
        # Check for queens attacking from bottom-right diagonal
        for x, y in zip(range(row, rows), range(col, cols)):
            if [x, y] in queens:
                res.append([x, y])
                break
            
        # Check for queens attacking from top-right diagonal
        for x, y in zip(range(row, -1, -1), range(col, cols)):
            if [x, y] in queens:
                res.append([x, y])
                break
        
        # Check for queens attacking from bottom-left diagonal
        for x, y in zip(range(row, rows), range(col, -1, -1)):
            if [x, y] in queens:
                res.append([x, y])
                break

        return res