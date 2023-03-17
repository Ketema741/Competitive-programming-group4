class Solution:
    def reverseWords(self, s: str) -> str:
        def reverse(left, right):
            while left < right:
                string[left], string[right] = string[right], string[left]
                left += 1
                right -= 1

        left = 0
        string = list(s)
        
        for right in range(len(s)):
            if string[right] == " ":
                reverse(left, right - 1)
                left = right + 1
                
        reverse(left, len(string) - 1)
        
        return "".join(string)