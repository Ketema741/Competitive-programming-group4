class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        N = len(prices)
        res = max_profit = 0
        left, right = 0, 1
        
        while right < N:
             
            
            while right < N and prices[right] >= prices[right-1]:
                right += 1
            
            max_profit = max(max_profit, prices[right - 1] - prices[left])
            
            res += max_profit
            max_profit = 0
            left = right
            right += 1
            
        return res