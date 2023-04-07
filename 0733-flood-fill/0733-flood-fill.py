class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        visited = set()
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        
        def inbound(row, col):
            return 0 <= row < len(image) and 0 <= col < len(image[0])
        
        def dfs(row, col, color):
            if not inbound(row, col) or image[row][col] != color:
                return
            
            image[row][col] = newColor
            
            for row_change, col_change in directions:
                dfs(row + row_change, col + col_change, color)
        
        color = image[sr][sc]
        
        if color == newColor:
            return image
        
        dfs(sr, sc, color)
        
        return image
