class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        left = bisect.bisect_left(nums, target)
        right = bisect.bisect_right(nums, target) - 1
      
        if -1 < left <= right < len(nums):
            return [left, right]
            
        return [-1, -1]