class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        pair_count = 0
        
        for row in grid:
            for column in zip(*grid):
                if tuple(row) == column:
                    pair_count += 1
        return pair_count