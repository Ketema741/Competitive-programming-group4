class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        graph = defaultdict(set)
        res = 0
        
        for city1, city2 in roads:
            graph[city1].add(city2)
            graph[city2].add(city1)
            
        for i in range(n):
            for j in range(i+1,n):
                
                connection = i in graph[j]
                
                res = max(res, len(graph[i]) + len(graph[j]) - connection)
                
                
        return res
                