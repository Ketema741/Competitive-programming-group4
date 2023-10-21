class Solution:
    def arraySign(self, nums: List[int]) -> int:
        if 0 in nums:
            return 0
        count_neg = 0

        for num in nums:
            if num < 0:
                count_neg += 1
        
        if count_neg % 2 == 0:
            return 1
            
        return -1