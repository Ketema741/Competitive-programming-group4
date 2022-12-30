class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        total = 0
        nums.sort(reverse=True)
        
        for right in range(1, len(nums)):
            if right+1 < len(nums):
                if  nums[right-1] < (nums[right] + nums[right+1]):
                    total = (nums[right-1] + nums[right]+ nums[right + 1])
                    return total            
        return total
            
        
        