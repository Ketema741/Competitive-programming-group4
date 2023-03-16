class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        arr2.sort()
        n = len(arr2)-1
        
        def isValid(num):
            left, right = 0, n
            while left <= right:
                mid = left + (right - left)//2
                
                if abs(num - arr2[mid]) <= d:
                    return False
                    
                if arr2[mid] > num:
                    right = mid - 1
                else:
                    left = mid + 1
            return True
    
        return sum( isValid(num) for num in arr1)