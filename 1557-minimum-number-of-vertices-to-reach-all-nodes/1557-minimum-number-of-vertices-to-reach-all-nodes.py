class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        incomingEdges = set()
        res = []
        for out_, in_ in edges:
            incomingEdges.add(in_)
        
    
        for i in range(n):
            if i not in incomingEdges:
                res.append(i)
        
        return res