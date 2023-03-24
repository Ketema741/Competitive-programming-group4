class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        res = []
        for num in nums:
            indx = abs(num) - 1
            nums[indx] = -1*abs(nums[indx])
            
        for indx, num in enumerate(nums):
            if num > 0:
                res.append(indx + 1)
                
        return res