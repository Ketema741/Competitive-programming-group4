class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        res = s.split()
        print(s.split())
        return  len(res[-1])
