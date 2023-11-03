class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        
        if nums[0] < nums[-1]:
            return nums == sorted(nums)
        else:
            return nums == sorted(nums, reverse=True)