class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        
        gaussionSum = n*(n+1)//2
        
        return   gaussionSum - sum(nums)
    
    
    """
        CYCLIC SORT
        i = 0
        while i < len(nums):
            j = nums[i]
            if j < len(nums) and nums[i] != nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
            else:
                i += 1
                
        for i in range(len(nums)):
            if nums[i] != i:
                return i
            
        return len(nums)
        
       BIT MANIPULATION
        res = nums[0] ^ 0
        for i in range(1, len(nums)):
            res = res ^ nums[i] ^ i
            
        return res^len(nums)
        
        MATHS
        res = len(nums)

        for i in range(len(nums)):
            res += i - nums[i]
        return res
    """