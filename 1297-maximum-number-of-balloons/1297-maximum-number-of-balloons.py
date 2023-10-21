class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        countText = defaultdict(int)
        for char in text:
            countText[char] += 1

        balloon = {"b": 1, "a": 1, "l": 2, "o": 2, "n": 1}

        res = len(text)
        
        for c in balloon:
            res = min(res, countText[c] // balloon[c])
            
        return res
        