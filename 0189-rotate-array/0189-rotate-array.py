class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        k = k % len(nums)
        k1 = k -  1
        
        left, right = 0, len(nums) - 1    
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
            
        right = len(nums) - 1
        while k < right:
            nums[k], nums[right] = nums[right], nums[k]
            k += 1
            right -= 1
            
        left = 0
        while left < k1:
            nums[k1], nums[left] = nums[left], nums[k1]
            k1 -= 1
            left += 1
        return nums
            
            
            
"""
    nums2 = [0] * k     
    while k:
        nums2[k-1] = nums.pop()
        k -= 1
            
    for num in nums2[::-1]:
        nums.insert(0,num)

"""