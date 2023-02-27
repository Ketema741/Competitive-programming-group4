class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        basket = {}
        res = left = 0
        
        for right, fruit in enumerate(fruits):
            basket[fruit] = 1 + basket.get(fruit, 0)
            
            while len(basket)> 2:
                basket[fruits[left]] -= 1
                if basket[fruits[left]] == 0:
                       basket.pop(fruits[left])
                left += 1
                
            res = max(res, right - left +1)
            
        return res