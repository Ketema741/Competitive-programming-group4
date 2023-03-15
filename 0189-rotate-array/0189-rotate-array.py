class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        def reverse(left, right):
            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
                
        k = k % len(nums)        
        left, right = 0, len(nums) - 1
        
        reverse(left, right)
        reverse(k, right)
        reverse(0, k-1)