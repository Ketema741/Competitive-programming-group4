class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        max_val = max(nums)
        num2 = max_val + k
        
        total_sum = sum(range(max_val, num2))
        
        return total_sum