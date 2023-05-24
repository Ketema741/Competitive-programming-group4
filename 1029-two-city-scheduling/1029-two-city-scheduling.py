class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        difference = []
        
        for index in range(len(costs)):
            a, b = costs[index]
            difference.append([a-b, index])
            
        difference.sort()
        
        res = 0
        
        left = 0
        
        for i in range(len(costs)//2):
            res += costs[difference[i][1]][0]
            
        for i in range(len(costs)//2, len(costs)):
            res += costs[difference[i][1]][1]
        
        return res