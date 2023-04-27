class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        graph = defaultdict(list)
        visited = set()
        
        for node1, node2 in edges:
            graph[node1].append(node2)
            graph[node2].append(node1)
            
            
        def dfs(node):
            if node in visited:
                return 0
            
            visited.add(node)
            time = 0
            
            for nei in graph[node]:
                time += dfs(nei)
            
            if node == 0:
                return time
            
            
                
            if hasApple[node] or time:
                time += 2
           
                
            return time
        
        return dfs(0)
            