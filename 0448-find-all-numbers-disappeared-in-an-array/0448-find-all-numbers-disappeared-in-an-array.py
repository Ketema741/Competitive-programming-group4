class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        res = []
#         for num in nums:
#             indx = abs(num) - 1
#             nums[indx] = -1*abs(nums[indx])
            
#         for indx, num in enumerate(nums):
#             if num > 0:
#                 res.append(indx + 1)
                
#         return res
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