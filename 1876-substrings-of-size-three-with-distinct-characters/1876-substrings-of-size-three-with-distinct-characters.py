class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        res = 0
        window = {}
        
        left = 0
        for right in range(len(s)):
            window[s[right]] = 1 + window.get(s[right], 0)
            
            while right - left + 1 > 3:
                window[s[left]] -= 1
                if window[s[left]] == 0:
                    window.pop(s[left])
                    
                left += 1
                    
            if len(window) == 3:
                res += 1
                
        return res