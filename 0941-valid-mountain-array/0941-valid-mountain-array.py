class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        move_right = 0
        
        # Check if increasing
        while move_right + 1 < len(arr) and arr[move_right] < arr[move_right + 1]:
            move_right += 1
        
        
        if move_right == 0 or move_right == len(arr) - 1:
            return False
        
        # Check if decreasing
        while move_right + 1 < len(arr) and arr[move_right] > arr[move_right + 1]:
            move_right += 1
            
        # Return True if valid mountain array
        return move_right == len(arr) - 1
