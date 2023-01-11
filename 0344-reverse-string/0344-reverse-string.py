class Solution:
    def reverseString(self, s: List[str]) -> None:
        left, right = 0, len(s) - 1
        while right > left :
            s[left], s[right] = s[right], s[left]
            right -= 1
            left += 1
