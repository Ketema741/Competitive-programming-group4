class Solution:        
    def strStr(self, haystack: str, needle: str) -> int:
        N, M = len(needle), len(haystack)
        if N > M:
            return -1

        if not needle:
            return 0

        LPS = [0] * N
        prev, i = 0, 1

        while i < N:
            if needle[i] == needle[prev]:
                prev += 1
                LPS[i] = prev
                i += 1
            elif prev == 0:
                LPS[i] = 0
                i += 1
            else:
                prev = LPS[prev - 1]

        i = 0  # haystack
        j = 0  # needle

        while i < M:
            if haystack[i] == needle[j]:
                i += 1
                j += 1
            elif j == 0:
                i += 1
            else:
                j = LPS[j - 1]

            if j == N:
                return i - N

        return -1
