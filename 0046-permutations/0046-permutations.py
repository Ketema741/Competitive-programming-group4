class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        def permutation(temp, nums):
            if len(temp) == len(nums):
                res.append(temp[:])
                return
            
            
            for num in nums:
                if num not in temp :
                    temp.append(num)
                    permutation(temp, nums)
                    temp.pop()
                    
        permutation([], nums)
        
        return res