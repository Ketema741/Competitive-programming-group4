class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        res = []
        
        def backtrack(indx, nums):
            if indx == len(nums) and len(res) >= 3:
                return True  
            
            for i in range(indx, len(nums)):
                if nums[indx] == "0" and i != indx : 
                    return False
                
                n= int(nums[indx:i+1])
                
                if len(res) >= 2 and res[-2] + res[-1] < n: 
                    return False
                
                if len(res) <= 1 or res[-2] + res[-1] == n:
                    res.append(n)# choose
                    
                    if backtrack(i+1,  nums): # explore
                        return True
                    
                    res.pop() # unchoose
            
            return False
    
        backtrack(0, num)
        return len(res) > 0