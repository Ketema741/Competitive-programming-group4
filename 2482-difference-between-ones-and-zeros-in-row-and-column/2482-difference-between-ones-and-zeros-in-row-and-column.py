class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        # Get the dimensions of the grid
        rows, cols = len(grid), len(grid[0])
        
        # Initialize the diff grid
        diff = [[0 for _ in range(cols)] for _ in range(rows)]
        
        # Create a hash_map to store count of ones and zeros in rows and columns
        hash_map = defaultdict(int)
        
        # Count the number of ones and zeros in each row and column
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    hash_map[(row, 'r1')] += 1
                    hash_map[(col, 'c1')] += 1
                    
                else:
                    hash_map[(row, 'r0')] += 1
                    hash_map[(col, 'c0')] += 1
        
        # Compute the diff matrix
        for row in range(rows):
            for col in range(cols):
                diff[row][col] = hash_map[(row, 'r1')] + hash_map[(col, 'c1')] - hash_map[(row, 'r0')] - hash_map[(col, 'c0')]
        return diff