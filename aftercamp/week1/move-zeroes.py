class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        left = right = 0
        N = len(nums) - 1
        
        while right < N:
            if nums[right] != 0:
                right += 1
                left += 1
                
            while right < N and nums[right] == 0:
                right += 1
                
            if left < right and nums[left] == 0:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1