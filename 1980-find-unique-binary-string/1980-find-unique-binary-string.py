class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        strSet = { s for s in nums}
        
        
        def backtrack(indx, curr):
            if indx == len(nums):
                res = ''.join(curr)
                if res not in strSet:
                    return res
                return None
            
            
            res = backtrack(indx+1, curr + ["0"])
            if res: return res
            
            res = backtrack(indx+1, curr + ["1"])
            if res: return res
        return backtrack(0, [])
            