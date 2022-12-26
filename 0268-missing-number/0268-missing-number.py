class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        all_nums = [num for num in range(len(nums)+1)]
        
        res = list(set(all_nums) - set(nums))
       
        if res:
            return res[0]
        return 0