class Solution:
    def printVertically(self, s: str) -> List[str]:
        words = s.split(' ')
        max_len = max(len(word) for word in words)
        res = []
        for i in range(max_len):
            l = []
            for word in words:
                l.append(word[i] if i < len(word) else ' ')
            res.append(''.join(l).rstrip())
        return res
    
    
    """
    
     
        
    """