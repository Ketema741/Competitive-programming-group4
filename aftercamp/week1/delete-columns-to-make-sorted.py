class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        res = 0
        
        # traversing column wise          
        for col in range(len(strs[0])):
             for row in range(1, len(strs)):
                # for a given column check if the previous char is greater than the current or unsorted
                if  strs[row - 1][col] > strs[row][col]:
                    res += 1
                    break

        return res