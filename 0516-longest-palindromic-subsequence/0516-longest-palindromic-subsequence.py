class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        cache = {}
        
        def dfs(l, r):
            if r < 0 or l > len(s)-1:
                return 0
            
            if (l,r) in cache:
                return cache[(l, r)]

            if s[l]==s[r]:
                cache[(l, r)] = 1 + dfs(l + 1, r - 1 )
            else:
                cache[(l, r)] = max(dfs(l + 1, r), dfs(l, r - 1))
                
            return cache[(l, r)]
        
        dfs(0, len(s) - 1)
        return max(cache.values())

