class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        res = []
        
        left, right = 0, len(nums) - 1
        
        while left <= right:
            leftSqr, rightSqr = nums[left]**2, nums[right]**2
            
            if leftSqr < rightSqr:
                res.append(rightSqr)
                right -= 1
            else:
                res.append(leftSqr)
                left += 1
                
        return res[::-1]