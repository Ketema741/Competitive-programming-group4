class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        count, res = 0, []
        N = len(nums)
        for index in range(N):
            if index + 1 < N and nums[index + 1] == nums[index]:
                nums[index] *= 2
                nums[index + 1] = 0
        
        for i, num in enumerate(nums):
            if num != 0:
                res.append(num)
            else: count += 1
        while count:
            res.append(0)
            count -= 1
        return res
                