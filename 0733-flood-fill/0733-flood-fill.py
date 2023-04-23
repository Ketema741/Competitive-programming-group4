class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        
        def inbound(row, col):
            return 0 <= row < len(image) and 0 <= col < len(image[0])
        
        def dfs(row, col, color):
            image[row][col] = newColor
            
            for row_change, col_change in directions:
                new_row = row + row_change
                new_col = col + col_change

                if inbound(new_row, new_col) and image[new_row][new_col] == color:
                    dfs(new_row, new_col, color)
        
        color = image[sr][sc]
        
        if color == newColor:
            return image
        
        dfs(sr, sc, color)
        
        return image