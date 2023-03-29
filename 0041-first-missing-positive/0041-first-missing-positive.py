class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        i = 0
        while i < len(nums):
            j = nums[i] - 1
            
            
            if nums[i] > 0 and j < len(nums) and nums[i] != nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
            else:
                i += 1
        i = 0
        while i < len(nums):
            if nums[i] != i + 1:
                return i + 1
            i += 1
            
        return i+1
