class Solution:   
    def findKthBit(self, n: int, k: int) -> str:
        res = []
        
        def invert(st):
            curStr = ''
            for num in st:
                if num == '0':
                    curStr += '1'
                else:
                    curStr += '0'
                    
            return curStr[::-1]
        
        
        def recursive(s, res):
            if len(res) == n:
                return  res
            
            new = s + '1' + invert(s)
            res.append(new)
            recursive(new, res)
            
            return res[n-1][k-1]
            
        return recursive('0',[])