class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        k -= 1
        vowels = {'a', 'e', 'i', 'o', 'u'}
        
        res = 0
        
        left = 0
        count = 0
        for right in range(len(s)):
            
            while right - left > k:
                if s[left] in vowels:
                    count -= 1
                left += 1
                
            if s[right] in vowels:
                count += 1
                
            res = max(res, count)
            
        return res
    """
    left = 0        coutn = 0       res = 0
    
    r = 0, l = 0, k =  2
    
    0 - 0 > k false     count = 0
    1 - 0 > k false     count = 1
    
    
    """