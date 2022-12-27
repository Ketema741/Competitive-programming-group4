class Solution:
    def interpret(self, command: str) -> str:
        res = []
        
        for indx, char in enumerate(command):
            if char not in '()':
                res.append(char)
            if char == '(' :
                res.append("(")
            if char == ")":
                top = ""
                while res[-1] != "(":
                    top += res.pop()
                top += res.pop()
                if top == "(":
                    res.append("o")
                else:
                    res.append("al")
                    
        return ''.join(res)