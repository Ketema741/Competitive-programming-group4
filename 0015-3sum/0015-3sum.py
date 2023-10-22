class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        nums.sort()

        for indx, num in enumerate(nums):
            if indx > 0 and num == nums[indx - 1]:
                continue

            left, right = indx + 1, len(nums) - 1
            
            while left < right:
                three_sum = num + nums[left] + nums[right]
                
                if three_sum > 0:
                    right -= 1
                elif three_sum < 0:
                    left += 1
                else:
                    res.add((num, nums[left], nums[right]))
                    left += 1
                    
        return [list(triblets) for triblets in res]
