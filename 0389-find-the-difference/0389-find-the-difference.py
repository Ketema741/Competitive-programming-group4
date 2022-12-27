class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        hash_table_S = {}
        hash_table_t = {}
        res = ""
        for char in s:
            hash_table_S[char] = 1 + hash_table_S.get(char, 0)
        
        for char in t:
            hash_table_t[char] = 1 + hash_table_t.get(char, 0)
            
        for char in hash_table_t.keys():
            if hash_table_t[char] != hash_table_S.get(char, 0):
                res += char

        return res
    
    
    
                
        """
        
        a         a
        b         b
        c         c
        d         d
                  e
        """