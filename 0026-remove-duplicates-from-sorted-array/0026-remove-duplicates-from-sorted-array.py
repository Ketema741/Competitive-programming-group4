class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 1
        
        for i in range(len(nums) - 1):
            if nums[i] != nums[i + 1]:
                nums[k] = nums[i + 1]
                k += 1
                
        return k
            