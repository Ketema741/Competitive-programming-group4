class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(list)
        for i, eq in enumerate(equations):
            a, b = eq
            graph[a].append((b, values[i]))
            graph[b].append((a, 1/values[i]))
        
        def bfs(src, target):
            if src not in graph or target not in graph:
                return -1
            
            queue = deque([(src, 1)])
            visited = set()
            visited.add(src)
            
            while queue:
                node, w = queue.popleft()
                if node == target:
                    return w
                
                visited.add(node)
                for nei, weight in graph[node]:
                    if nei not in visited:
                        queue.append((nei, w * weight))
            return -1
        
        return [bfs(src, target) for src, target in queries]