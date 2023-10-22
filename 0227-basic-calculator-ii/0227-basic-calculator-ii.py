class Solution:
    def calculate(self, s: str) -> int:
        stack, cur, operator = [], 0, "+"
        allOperator = {'+','-','/','*'}
        nums = [str(x) for x in range(10)]
        for indx in range(len(s)):
            char = s[indx]
            if char in nums:
                cur = cur * 10 + int(char)
            if char in allOperator or indx == len(s)-1:
                if operator == '+':
                    stack.append(cur)
                if operator == '-':
                    stack.append(-cur)
                if operator == '*':
                    stack[-1] *= cur
                if operator == '/':
                    stack[-1] = int(stack[-1] / cur)
                cur = 0
                operator = char
        return sum(stack)
                    
        