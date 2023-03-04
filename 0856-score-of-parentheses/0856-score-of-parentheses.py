class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []
        
        for i in s:
            if i == "(":
                stack.append(i)
            elif stack[-1] == "(" and i == ")":
                stack.pop()
                stack.append(1)
            else:
                count = 0
                
                while stack[-1] != "(":
                    count += stack.pop()
                    
                if stack[-1] == "(":
                    stack.pop()
                    stack.append(count*2)
                    
        return sum(stack)