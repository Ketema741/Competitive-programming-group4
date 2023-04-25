class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        graph = defaultdict(list)
        colors = [-1] * (n + 1)
        
        for p1, p2 in dislikes:
            graph[p1].append(p2)
            graph[p2].append(p1)
            
        def dfs(node, node_color):
            
    
            colors[node] = node_color
            
            for nei in graph[node]:
                if colors[nei] == colors[node]:
                    return False
                
                if colors[nei] == -1:
                    if not dfs(nei, 1 - node_color):
                        return False
                    
            return True
        
        for i in range(1, n + 1):
            if colors[i] == -1:
                if not dfs(i, 0):
                    return False
                
        return True
        