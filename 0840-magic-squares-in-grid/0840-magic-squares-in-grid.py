class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        magic_count = 0

        # Helper function to check if a given 3x3 subgrid is a magic square or not
        def is_magic(subgrid):
            # Check if the set of numbers in the subgrid is equal to set of numbers from 1 to 9
            if set(subgrid) != set(range(1,10)):
                return False
            # Check if sum of rows, columns, and diagonals are equal to 15
            if (subgrid[0] + subgrid[1] + subgrid[2] != 15 or 
                subgrid[3] + subgrid[4] + subgrid[5] != 15 or 
                subgrid[6] + subgrid[7] + subgrid[8] != 15 or
                subgrid[0] + subgrid[3] + subgrid[6] != 15 or 
                subgrid[1] + subgrid[4] + subgrid[7] != 15 or 
                subgrid[2] + subgrid[5] + subgrid[8] != 15 or
                subgrid[0] + subgrid[4] + subgrid[8] != 15 or 
                subgrid[2] + subgrid[4] + subgrid[6] != 15):
                return False
            return True
        
        # Iterate over the grid with a window of size 3x3
        for row in range(rows-2):
            for col in range(cols-2):
                # Create a subgrid of size 3x3
                subgrid = [grid[i][j] for i in range(row,row+3) for j in range(col,col+3)]
                # Check if the subgrid is a magic square or not
                if is_magic(subgrid):
                    magic_count += 1
        return magic_count