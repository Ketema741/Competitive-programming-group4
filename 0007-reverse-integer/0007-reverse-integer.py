class Solution:
    def reverse(self, x: int) -> int:
        res = 0
        min_int, max_int = -2**31, 2**31-1
        
        while x:
            digit = int(math.fmod(x, 10))
            
            if (res > int(max_int / 10) or 
                (res == int(max_int / 10) and digit > int(math.fmod(max_int, 10)))):
                    return 0
                
            if (res < int(min_int / 10) or 
                (res == int(max_int / 10) and digit < int(math.fmod(min_int, 10)))):
                    return 0
                
            res = res * 10 + digit
            x = int(x / 10)
            
        return res