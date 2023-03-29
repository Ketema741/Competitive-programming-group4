class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        set_error = [0]*len(nums)
        duplicate, missing = -1, 0
        
        for num in nums:
            set_error[num-1] += 1
        
        for i in range(len(set_error)):
            if set_error[i] == 2:
                duplicate = i+1
                
            if set_error[i] == 0:
                missing = i+1
                
        return [duplicate, missing]
        
        