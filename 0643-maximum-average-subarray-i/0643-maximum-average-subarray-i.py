
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n = len(nums)
        res  = -math.inf
        left = sum_ = 0
        if n == k:
            return sum(nums) / k
        
        for right in range(n):
            sum_ += nums[right]
            
            if right - left > k - 1:
                sum_ -= nums[left]
                left += 1
                
            if right - left == k - 1:
                res = max(res, sum_)
                
        return res/k