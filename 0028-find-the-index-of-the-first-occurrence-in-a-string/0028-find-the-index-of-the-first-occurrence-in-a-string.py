class Solution:        
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) > len(haystack):
            return -1

        for i in range(len(haystack)):
            index = i + len(needle)

            if index <= len(haystack) and needle == haystack[i:index]:
                return i

        return -1