from collections import defaultdict

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        adj = defaultdict(list)

        for row in range(len(graph)):
            for col in range(len(graph[row])):
                adj[row].append(graph[row][col])

        res = []
        def dfs(node, visited):
            if node == len(graph) - 1:
                res.append(visited)
                return 
            
            for nd in adj[node]:
                dfs(nd, visited + [nd])

        dfs(0, [0])

        return res