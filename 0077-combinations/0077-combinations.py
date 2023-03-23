class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        def backtrack(start, comb):
            if len(comb) == k:
                res.append(comb.copy())
                return
            
            if start > n:
                return

            backtrack(start+1, comb + [start])
            backtrack(start+1, comb)


        backtrack(1, [])
        return res
