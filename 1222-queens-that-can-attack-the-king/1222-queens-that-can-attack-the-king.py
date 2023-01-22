class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        rows, cols = 8, 8
        row, col = king
        res = []

        for x in range(row, -1, -1):
            if [x, col] in queens:
                res.append([x, col])
                break

        for x in range(row, rows):
            if [x, col] in queens:
                res.append([x, col])
                break
                
        for y in range(col, -1, -1):
            if [row, y] in queens:
                res.append([row, y])
                break
        
        for y in range(col, cols):
            if [row, y] in queens:
                res.append([row, y])
                break
            
        for x, y in zip(range(row, -1, -1), range(col, -1, -1)):
            if [x, y] in queens:
                res.append([x, y])
                break
        
        for x, y in zip(range(row, rows), range(col, cols)):
            if [x, y] in queens:
                res.append([x, y])
                break
            
        for x, y in zip(range(row, -1, -1), range(col, cols)):
            if [x, y] in queens:
                res.append([x, y])
                break
        
        for x, y in zip(range(row, rows), range(col, -1, -1)):
            if [x, y] in queens:
                res.append([x, y])
                break

        return res