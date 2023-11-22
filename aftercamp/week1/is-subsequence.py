class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) > len(t):
            return False
        
        left = 0

        for right in range(len(t)):
            if left < len(s) and s[left] == t[right]:
                left += 1

        return len(s) == left