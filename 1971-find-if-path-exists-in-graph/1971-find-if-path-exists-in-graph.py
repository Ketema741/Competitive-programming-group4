class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        
        graph = defaultdict(list)
        def dfs(node, visited):
            if node == destination:
                return True
            
            visited.add(node)
            for neighbour in graph[node]:
                if neighbour not in visited:
                    found = dfs(neighbour, visited)
                    if found:
                        return True
            return False
        
        
        
        for v1, v2 in edges:
            graph[v1].append(v2)
            graph[v2].append(v1)
            
        visited = set()
        
        return dfs(source, visited)