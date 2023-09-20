class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        
        def dfs(i, cur, tot):
            if tot == target:
                res.append(cur.copy())
                return
            
            if tot > target or i >= len(candidates):
                return
            
            tot += candidates[i]
            cur.append(candidates[i])
            dfs(i, cur, tot)
            
            cur.pop()
            tot -= candidates[i]
            dfs(i+1, cur, tot)
            
        dfs(0, [], 0)
        
        return res
            
            