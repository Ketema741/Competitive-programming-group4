class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        
        def permutation(temp, nums):
            if len(nums) == 0:
                res.append(temp[:])
                return
            
            prev = -11
            for i in range(len(nums)):
                if prev == nums[i]:
                    continue
                    
                permutation(temp + [nums[i]], nums[:i] + nums[i+1:]) #explore
                prev = nums[i]
                    
        permutation([], nums)
        
        return res