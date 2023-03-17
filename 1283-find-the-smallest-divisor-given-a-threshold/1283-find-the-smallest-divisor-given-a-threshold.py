class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        left, right = 1, max(nums)
        res = inf
        
        while left <= right: 
            mid = left + (right - left)//2
            
            division_sum = sum(math.ceil(num/mid) for num in nums)
            
            if division_sum <= threshold:
                res = min(res, mid)
                right = mid - 1
            else:
                left = mid + 1
                
        return res
            