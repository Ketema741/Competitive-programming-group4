class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 1
        for indx in range(len(nums) - 1):
            
            if nums[indx] != nums[indx + 1] :
                nums[k] = nums[indx + 1]
                k += 1
                
        return(k)