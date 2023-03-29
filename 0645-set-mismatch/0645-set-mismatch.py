class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        duplicate, missing = -1, 0

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
                duplicate = nums[i]
                missing = i + 1
            
        return [duplicate, missing]