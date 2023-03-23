class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res = [-1]* (max(nums)+1)
        start = 0
        
        while start < len(nums):
            res[nums[start]] = nums[start] 
            start += 1
            
        for i in range(len(res)):
            if res[i] == -1:
                return i
            
        return len(res)