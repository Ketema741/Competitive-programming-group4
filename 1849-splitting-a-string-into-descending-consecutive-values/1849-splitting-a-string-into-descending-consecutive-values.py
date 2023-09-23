class Solution:
    def splitString(self, s: str) -> bool:
        
        def dfs(prev_val, indx):
            if indx == len(s) and prev_val != int(s):
                return True
            
            for i in range(indx, len(s)):
                val = int(s[indx:i+1])
                if prev_val == -1 or val + 1 == prev_val:
                    if dfs(val, i+1):
                        return True
                
            return False
        
        return dfs(-1, 0)