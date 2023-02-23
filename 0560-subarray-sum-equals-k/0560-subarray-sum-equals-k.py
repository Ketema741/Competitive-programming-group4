class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        curSum = res = 0
        prefixSum = {0:1}
        
        for num in nums:
            curSum += num
            diff = curSum - k 
            res += prefixSum.get(diff, 0)
            prefixSum[curSum] = 1 + prefixSum.get(curSum, 0)
            
        return res