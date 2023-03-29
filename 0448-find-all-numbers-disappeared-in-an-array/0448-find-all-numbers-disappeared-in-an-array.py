class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        res = []
        i = 0
        while i < len(nums):
            j = nums[i] - 1
            if nums[i] != nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
            else:
                i += 1
                
        for i in range(len(nums)):
            if nums[i] != i + 1:
                res.append(i+1)
            
        return res