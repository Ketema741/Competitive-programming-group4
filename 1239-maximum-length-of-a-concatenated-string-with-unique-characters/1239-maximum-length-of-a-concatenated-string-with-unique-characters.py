class Solution:
    def maxLength(self, arr: List[str]) -> int:
        charSet = set()
        
        def overlap(charSet, s):
            res = Counter(charSet) + Counter(s)
            return max(res.values()) > 1
        
        def backtrack(indx):
            if indx == len(arr):
                return len(charSet)
            
            res = 0
            if not overlap(charSet, arr[indx]):
                for c in arr[indx]:
                    charSet.add(c)
                    
                res = backtrack(indx + 1)
                
                for c in arr[indx]:
                    charSet.remove(c)
                    
            return max(res, backtrack(indx + 1))
            
        return backtrack(0)
                     