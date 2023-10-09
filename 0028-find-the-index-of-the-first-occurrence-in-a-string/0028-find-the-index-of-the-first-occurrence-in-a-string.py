class Solution:        
    def strStr(self, haystack: str, needle: str) -> int:
        targetHash = currHash = 0
        m = len(needle)
        
        power = 0
        for i in range(m - 1, -1, -1):
            pw = 27**power
            targetHash += (ord(needle[i]) - ord("a") + 1) * pw
            
            if i < len(haystack):
                currHash +=  (ord(haystack[i]) - ord("a") + 1) * pw
            power += 1
            
        if targetHash == currHash:
            return 0
        
        for i in range(len(haystack)):
            hashVal = ord(haystack[i]) - ord("a") + 1
            
            currHash -= hashVal * 27** (m - 1)
        
            if i + len(needle)  < len(haystack):
                currHash = currHash*27 + (ord(haystack[i + len(needle) ]) - ord("a") + 1)
            
            if targetHash == currHash:
                return i+1
            
        return -1