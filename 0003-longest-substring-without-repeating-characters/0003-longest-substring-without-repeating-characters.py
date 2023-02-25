class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        res = left = 0
        
        for right, char in enumerate(s):
            while char in charSet:
                charSet.remove(s[left])
                left += 1
            
            charSet.add(char)
            res = max(res, right - left + 1)
            
        return res
        