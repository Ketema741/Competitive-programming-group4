class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        i = self.bs(nums, target, True)
        j = self.bs(nums, target, False)
      
        return [i, j]

    def bs(self, nums, target, left_baise):
        left, right = 0, len(nums) - 1
        i = -1
        while left <= right:
            mid = left + (right - left)//2
            
            if nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                i = mid
                if left_baise:
                    right = mid - 1
                else:
                    left = mid + 1

        return i