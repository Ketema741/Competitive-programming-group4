class Solution:
    def smallestSubsequence(self, s: str) -> str:
        stack, hash_map = [], defaultdict(int)
        
        for char in s:
            hash_map[char] += 1
        
        for char in s:
            if char in stack:
                hash_map[char] -= 1
                continue
            
            while stack and stack[-1] > char and hash_map[stack[-1]] > 0:
                stack.pop()
            
            hash_map[char] -= 1
            stack.append(char)
            
        return ''.join(stack)