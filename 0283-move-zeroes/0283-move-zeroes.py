class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        left = right = 0
        while right != len(nums)-1:
            if nums[right] != 0:
                right += 1
                left += 1
                
            while right != len(nums)-1 and nums[right] == 0:
                right += 1
                
            if left < right and nums[left] == 0:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1