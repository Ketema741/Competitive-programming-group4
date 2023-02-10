class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        
        for indx in range(len(nums)):
            if nums[indx] != val:
                nums[k] = nums[indx]
                k += 1
                
        return k