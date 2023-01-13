class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        deleted_cols = 0
        
        # traversing column wise          
        for col_idx in range(len(strs[0])):
             for row_idx in range(1, len(strs)):
                
                # for a given column check if the previous char is greate than the current  which means unsorted
                if  strs[row_idx - 1][col_idx] > strs[row_idx][col_idx]:
                    deleted_cols += 1
                    break
        return deleted_cols