class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        max_ = 0
        
        for sentence in sentences:
            max_ = max(max_, len(sentence.split(" ")))
            
        return max_