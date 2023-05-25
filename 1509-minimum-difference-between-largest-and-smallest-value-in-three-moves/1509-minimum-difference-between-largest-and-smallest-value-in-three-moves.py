class Solution:
    def minDifference(self, nums: List[int]) -> int:
        
        if len(nums) < 5:
            return 0
        nums.sort()
        
        
        
        for i in range(3):
            if (nums[3 - i]  - nums[0]) > ( nums[-1] - nums[-4 + i]):
                nums.pop(0)

            else:
                nums.pop()

        return nums[-1] - nums[0]
        
        