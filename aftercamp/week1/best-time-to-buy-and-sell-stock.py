class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        left = 0
        
        for right in range(len(prices)): 
            if prices[right] < prices[left]:
                left = right
                
            res = max(res, prices[right] - prices[left])
        return res