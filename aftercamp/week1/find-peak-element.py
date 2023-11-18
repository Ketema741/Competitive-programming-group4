class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        res = 0
        N = len(nums) - 1

        left, right = 0, N

        while left <= right:
            mid = left + (right - left)//2

            if mid > 0 and nums[mid] < nums[mid - 1]:
                right = mid - 1
            elif mid < N and nums[mid] < nums[mid + 1]:
                left = mid + 1
            else:
                return mid