class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        right = len(numbers) - 1
        left = 0
        
        while left < right:
            two_sum = numbers[left] + numbers[right]
            
            if two_sum == target:
                return [left+1, right+1]
            elif two_sum > target:
                right -= 1
            else:
                left += 1