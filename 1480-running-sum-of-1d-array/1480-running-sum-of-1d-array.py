class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        res = []
        runn_sum = 0
        
        for num in nums:
            runn_sum += num
            res.append(runn_sum)
            
        return res