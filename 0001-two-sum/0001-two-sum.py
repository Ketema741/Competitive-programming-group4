class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = []
        
        for left in range(len(nums)):
            for right in range(left + 1, len(nums)):
                if (nums[left] + nums[right]) == target:
                    res.append(left)
                    res.append(right)
                    
        return res
        