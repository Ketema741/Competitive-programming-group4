class Solution:
    def swapper(self, s, left, right):
        if left >= right:
            return s
        
        s[left], s[right] = s[right], s[left]
        
        return self.swapper(s, left + 1, right - 1)
    
    def reverseString(self, s: List[str]) -> None:
        left, right = 0, len(s) - 1
        
        res = self.swapper(s, left, right)
        
        return res