class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        div = num // 3
        
        sum_ = div-1 + div + div +1
        if sum_ == num:
            return [div-1, div, div+1]
        else:
            return []