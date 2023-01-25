class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        max_len = math.ceil(math.sqrt(c))
        left, right = 0, max_len
        
        while left <= right:
            sum_ = left**2 + right**2
            if sum_ == c:
                return True
            if sum_ > c:
                right -= 1
            else:
                left += 1
                
        return False