class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
       
        res = bisect_left(nums, target)
                
        return res