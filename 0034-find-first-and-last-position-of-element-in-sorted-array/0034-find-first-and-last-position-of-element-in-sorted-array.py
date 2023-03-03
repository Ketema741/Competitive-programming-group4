class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        low, high = 0, len(nums) - 1
        mid = (low + high)//2

        while low <= high:
            mid = low + (high - low) // 2
            
            if nums[mid] >= target:
                high = mid - 1
            else:
                low = mid + 1
        start = low
        
        if low < len(nums) and nums[low] == target:
            print('low')
            while low < len(nums)-1 and nums[low] == target:
                low += 1
            
            if nums[low] == target:
                return [start, low]
            else:
                return [start, low - 1]
                
        return [-1, -1]