class Solution:
    def printVertically(self, s: str) -> List[str]:
        words = s.split(' ')
        max_len = max(len(word) for word in words)
        res = []
        for indx in range(max_len):
            column_word = []
            for word in words:
                column_word.append(word[indx] if indx < len(word) else ' ')
            res.append(''.join(column_word).rstrip())
        return res
    
    
    """
    
     
        
    """