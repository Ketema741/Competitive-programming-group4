class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        inDegree = [0] * n
        graph = defaultdict(list)
        
        for node1, node2 in edges:
            graph[node1].append(node2)
            inDegree[node2] += 1
            
            
        queue = deque()
        ancestors = [set()] * n
        
        for i in range(n):
            if inDegree[i] == 0:
                queue.append(i)
                
        while queue:
            
            node = queue.popleft()
            
            for child in graph[node]:
                
                inDegree[child] -= 1
                ancestors[child] = ancestors[child].union(ancestors[node]).union({node})
                if inDegree[child] == 0:
                    queue.append(child)
                    
                
        res = []
        
        for i in range(len(ancestors)):
            res.append(sorted(ancestors[i]))
            
        return res
            
                
        
            
                
                