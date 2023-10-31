class Solution:
    def maxSubarrays(self, nums: List[int]) -> int:
        p = nums[0]

        for num in nums:
            p &= num
        
        if p != 0:
            return 1
        
        INF = (1 << 20) - 1 # 2^20 - 1
        res = 0
        curr = INF
        for num in nums:
            curr &= num

            if curr == 0:
                res += 1
                curr = INF
        
        return res