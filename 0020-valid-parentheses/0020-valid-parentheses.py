class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        hash_map = {")":"(","]":"[", "}":"{"}

        for char in s:
            if char in "([{":
                stack.append(char)
            elif not stack or hash_map[char] != stack.pop():
                    return False 

        return len(stack) == 0