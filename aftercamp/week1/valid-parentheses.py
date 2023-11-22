class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        hash_map = {"(":")","[":"]", "{":"}"}

        for char in s:
            if char in hash_map:
                stack.append(char)
            elif not stack or hash_map[stack.pop()] != char:
                    return False 

        return not stack