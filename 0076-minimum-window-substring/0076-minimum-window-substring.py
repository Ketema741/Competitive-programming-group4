class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""

        countT, window = {}, {}
        for char in t:
            countT[char] = 1 + countT.get(char, 0)

        have, need = 0, len(countT)
        res, resLen = [-1, -1], float("infinity")
        left = 0
        for right in range(len(s)):
            char = s[right]
            window[char] = 1 + window.get(char, 0)

            if char in countT and window[char] == countT[char]:
                have += 1

            while have == need:
                # update our result
                if (right - left + 1) < resLen:
                    res = [left, right]
                    resLen = right - left + 1
                # pop from the left of our window
                window[s[left]] -= 1
                
                if s[left] in countT and window[s[left]] < countT[s[left]]:
                    have -= 1
                left += 1
                
        left, right = res
        return s[left : right + 1] if resLen != float("infinity") else ""