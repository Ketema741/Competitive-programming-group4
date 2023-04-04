class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        target = 0
        count = 0
        
        for num in nums:
            target |= num
            
        def backtrack(OR, index):
            nonlocal count
            if OR == target:
                count += 1
                
            if index == len(nums):
                return
            
            for i in range(index, len(nums)):
                new_OR = OR | nums[i]
                backtrack(new_OR, i + 1)
                
        backtrack(0, 0)
            
        return count