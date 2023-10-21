class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        res = []

        for num in nums:
            n = abs(num) - 1
            nums[n] = -abs(nums[n])

        for i, num in enumerate(nums):
            if num > 0:
                res.append(i+1)
                
        return res