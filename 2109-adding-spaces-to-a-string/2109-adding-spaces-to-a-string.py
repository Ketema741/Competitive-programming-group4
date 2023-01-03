class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        result = s[:spaces[0]] + ' '
        last_indx = spaces[0]
        
        for indx  in range(1, len(spaces)):
            result += s[last_indx:spaces[indx]] + ' '
            last_indx = spaces[indx]
        result += s[last_indx:]
                         
        return result