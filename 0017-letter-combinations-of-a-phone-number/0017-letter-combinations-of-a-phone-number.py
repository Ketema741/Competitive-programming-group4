class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        res = []
        digitToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        
        def backtrack(indx, curr):
            if len(digits) == len(curr):
                res.append(curr)
                return
            for char in digitToChar[digits[indx]]:
                backtrack(indx + 1, curr+char)
        if digits:
            backtrack(0, "")
            
        return res