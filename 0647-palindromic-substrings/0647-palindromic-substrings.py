class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0

        def countPal(l, r):
            count = 0
            while l >= 0 and r < len(s) and s[l] == s[r]:
                count += 1
                l -= 1
                r += 1

            return count

        for i in range(len(s)):
            res += countPal(i, i)
            res += countPal(i , i + 1)
        
        return res
