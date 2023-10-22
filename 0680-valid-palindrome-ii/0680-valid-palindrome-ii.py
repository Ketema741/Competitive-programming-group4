class Solution:
    def validPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1

        while right > left:
            if s[left] != s[right]:
                skipL = s[left + 1:right + 1]
                skipR = s[left:right]
                
                return (skipL == skipL[::-1]) or (skipR == skipR[::-1])

            right -= 1
            left += 1

        return True
