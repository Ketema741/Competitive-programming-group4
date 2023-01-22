class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        rows, cols = len(grid), len(grid[0])
        diff = [[0 for _ in range(cols)] for _ in range(rows)]
        hash_map = defaultdict(int)
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    hash_map[(row, 'r1')] += 1
                    hash_map[(col, 'c1')] += 1
                    
                else:
                    hash_map[(row, 'r0')] += 1
                    hash_map[(col, 'c0')] += 1
        for row in range(rows):
            for col in range(cols):
                diff[row][col] = hash_map[(row, 'r1')] + hash_map[(col, 'c1')] - hash_map[(row, 'r0')] - hash_map[(col, 'c0')]
        return diff