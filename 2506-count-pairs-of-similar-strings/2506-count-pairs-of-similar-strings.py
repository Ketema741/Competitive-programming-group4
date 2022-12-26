class Solution:
    def similarPairs(self, words: List[str]) -> int:
        res = 0
        
        for indx, word in enumerate(words):
            word = set(word)
            
            for next_word in words[indx+1:]:
                if word == set(next_word):
                    res += 1
                    
        return res