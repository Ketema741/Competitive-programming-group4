class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        target = sum(nums) - x
        max_window = -1
        cur_sum = 0
        left = 0

        for right in range(len(nums)):
            cur_sum += nums[right]


            while left <= right and cur_sum > target:
                cur_sum -= nums[left]
                left += 1
                
            if cur_sum == target:
                max_window = max(max_window, right - left + 1)
        
        return -1 if max_window == -1 else  len(nums) - max_window

