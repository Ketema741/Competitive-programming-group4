from collections import defaultdict, deque
from typing import List

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        indegree = [0] * n
        
        if n <= 2:
            return [i for i in range(n)]
        
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
            indegree[u] += 1
            indegree[v] += 1
        
        leaves = deque([])
        for i in range(n):
            if indegree[i] == 1:
                leaves.append(i)
                
        while n > 2:
            n -= len(leaves)
            size = len(leaves)
            for _ in range(size):
                if leaves:
                    node = leaves.popleft()
                    
                    for child in graph[node]:
                        indegree[child] -= 1
                        if indegree[child] == 1:
                            leaves.append(child)
                        
        return list(leaves)
