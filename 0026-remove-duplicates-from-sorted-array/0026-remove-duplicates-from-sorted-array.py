class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left = 1
        
        for right in range(len(nums) - 1):
            if nums[right] != nums[right + 1]:
                nums[left] = nums[right + 1]
                left += 1
                
        return left
            