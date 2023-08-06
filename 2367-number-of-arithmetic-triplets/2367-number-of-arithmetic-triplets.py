class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        res = 0
        n = len(nums)
        
        for i in range(n):
            if nums[i] + diff in nums and nums[i] + 2 * diff in nums:
                res += 1
        
        return res