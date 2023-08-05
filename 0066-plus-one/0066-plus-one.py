class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        sum_ = 0
        
        for i,num in enumerate(digits[::-1]):
            sum_ += num*10**i
            
        sum_ += 1
        res = []
        
        for num in str(sum_):
            res.append(int(num))
            
        return res