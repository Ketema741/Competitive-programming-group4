class Solution:
    
    def __init__(self):
        self.idx = 0
            
    def decode(self, s, mult=1) -> str:
        curnt_str = ''

        while self.idx < len(s):
            if s[self.idx].isdigit():
                curnt_mult = ''

                while s[self.idx].isdigit():
                    curnt_mult += s[self.idx]
                    self.idx += 1

                self.idx += 1
                curnt_str += self.decode(s, mult = int(curnt_mult))

            elif s[self.idx].isalpha():
                curnt_str += s[self.idx]
                self.idx += 1

            else:
                self.idx += 1
                return mult*curnt_str

        return mult*curnt_str

        
        
    def decodeString(self, s: str) -> str:
        if len(s) == 1:
            return '' if s[0].isdigit() else s[0]            
        res = self.decode(s)
        
        return res