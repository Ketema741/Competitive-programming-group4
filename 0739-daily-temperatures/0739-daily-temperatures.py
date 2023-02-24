class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []
        
        for right, num in enumerate(temperatures):
            
            while stack and num > temperatures[stack[-1]]:
                left = stack.pop()
                res[left] = right - left
            
            stack.append(right)
            
        return res
        