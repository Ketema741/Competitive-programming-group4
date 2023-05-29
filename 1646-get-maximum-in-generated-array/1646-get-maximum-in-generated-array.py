class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        max_ = 0
        
        if n < 2:
            return n
        nums = [0 for i in range(n+1)]
        
        nums[0], nums[1] = 0, 1
        
        for i in range(2, n+1):
            nums[i] = nums[i//2]
            
            if i%2 != 0:
                nums[i] += nums[i//2 +1]
                
            max_ = max(max_, nums[i])
            
        return max_
        
        
        