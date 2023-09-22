from typing import List

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []
        part = []

        def isValidIP(i):
            return 0 <= int(i) <= 255

        def dfs(i, dots):
            if i == len(s) and dots == 4:
                res.append(".".join(part))
                return
            if dots >= 4:
                return

            for j in range(i, min(i+3, len(s))):
                if isValidIP(s[i:j+1]) and (j == i or s[i] != "0"):
                    part.append(s[i:j+1])
                    dfs(j+1, dots+1)
                    part.pop()

        dfs(0, 0)
        return res
