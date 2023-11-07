class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []
        
        for par in s:
            if par == "(":
                stack.append(par)
            elif stack[-1] == "(" and par == ")":
                stack.pop()
                stack.append(1)
            else:
                count = 0
                
                while stack[-1] != "(":
                    count += stack.pop()
                    
                if stack[-1] == "(":
                    stack.pop()
                    stack.append(count * 2)
                    
        return sum(stack)