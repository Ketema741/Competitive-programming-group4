class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        if len(strs) == 0:
            return ""
        
        shortest = min(strs, key=len)
       
        for indx, char in enumerate(shortest):
            
            for word in strs:
                if word[indx] != char:
                    return shortest[:indx]
                
        return shortest
        
   
