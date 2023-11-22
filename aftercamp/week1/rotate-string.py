class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if s == goal:
            return True

        for i in range(len(s)):
            s = s[1:] + s[:1]
            if s == goal:
                return True

        return False