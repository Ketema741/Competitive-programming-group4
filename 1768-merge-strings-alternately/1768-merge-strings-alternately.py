class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str: 
        N = max(len(word1), len(word2))
        res = ""
        
        for indx in range(N):
            if indx < len(word1):
                res += word1[indx]
                
            if indx < len(word2):
                res += word2[indx]
                
        return res