class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        for row in range(rows):
            if matrix[row][-1] < target:
                continue

            for col in range(cols):
                left, right = 0, cols
                while left <= right:
                    mid = left + (right - left)//2

                    if matrix[row][mid] > target:
                        right = mid - 1
                    elif matrix[row][mid] < target:
                        left = mid + 1
                    else:
                        return True
                
                return False
"""
    n = len(matrix)
    m = len(matrix[0])
    
    Time complexity = O(n + m)
    space complexity = O(1)
""" 