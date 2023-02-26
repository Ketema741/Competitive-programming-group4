class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = list()
        
        for i in range(len(num)):
            while stack and stack[-1] > num[i] and k:
                stack.pop()
                k-=1
            
            if stack or num[i] is not '0':
                stack.append(num[i])
        
        if k: stack = stack[0:-k]    
        
        return ''.join(stack) or '0'
            
                