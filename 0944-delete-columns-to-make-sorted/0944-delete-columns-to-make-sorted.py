class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        count = 0
        for col_idx in range(len(strs[0])):
             for row_idx in range(1, len(strs)):
                if  strs[row_idx - 1][col_idx] > strs[row_idx][col_idx]:
                    count += 1
                    break
        return count