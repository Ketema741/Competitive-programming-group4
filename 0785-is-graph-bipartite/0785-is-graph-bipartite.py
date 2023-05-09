class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        colors = [-1] * len(graph)
        adj_list = defaultdict(list)
        
        # populate adjacency list from graph
        for node, neighbors in enumerate(graph):
            adj_list[node] = neighbors
        
        def dfs(node, color):
            if colors[node] != -1:
                return colors[node] == color
            
            colors[node] = color
            
            for neighbor in adj_list[node]:
                if not dfs(neighbor, 1 - color):
                    return False
                
            return True
        
        for i in range(len(graph)):
            if colors[i] == -1:
                if not dfs(i, 0):
                    return False
        return True
