class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        na, nb = len(a), len(b)
        n = nb // na
        tmp = a * n

        if b in tmp:
            # if b = "abcdabcd"
            return n

        tmp += a
        if b in tmp:
            # if b = "cdabcdab" (prefix match && suffix match)
            return n + 1

        tmp += a
        if b in tmp:
            # if b = "cdabcdabcdab"
            return n + 2

        return -1
