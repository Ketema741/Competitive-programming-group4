class Solution:
    def maxProduct(self, words: List[str]) -> int:
        masks = []
        n = len(words)
        
        for word in words:
            mask = 0
            for char in word:
                bit=ord(char)-ord('a')
                mask |= (1<<bit)
                
            masks.append(mask)
            
        res = 0
        for i in range(n):
            for j in range(n):
                if i != j:
                    if (masks[i] & masks[j]) == 0:
                        res = max(res, len(words[i])*len(words[j]))
                        
        return res