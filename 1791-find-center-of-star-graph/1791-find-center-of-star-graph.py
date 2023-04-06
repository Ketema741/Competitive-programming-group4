class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        firstEdge, secondEdge = edges[0], edges[1]
        
        for val in firstEdge:
            if val in secondEdge:
                return val