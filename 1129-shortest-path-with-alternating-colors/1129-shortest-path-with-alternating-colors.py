class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        red = defaultdict(list)
        blue = defaultdict(list)
        queue = deque([])
        visited = set()
        res = [-1 for _ in range(n)]
        
        for src, dest in redEdges:
            red[src].append(dest)
            
        for src, dest in blueEdges:
            blue[src].append(dest)
            
        visited.add((0, None))
        queue.append([0, 0, None])
        
        while queue:
            node, length, edge_color = queue.popleft()
            
            if res[node] == -1:
                res[node] = length
            
            if edge_color != 'red':
                for nei in red[node]:
                    if (nei, 'red') not in visited:
                        queue.append([nei, length + 1, 'red'])
                        visited.add((nei, 'red'))
            
            if edge_color != 'blue':
                for nei in blue[node]:
                    if (nei, 'blue') not in visited:
                        queue.append([nei, length + 1, 'blue'])
                        visited.add((nei, 'blue'))
        return res
                    
                    
            
                
            