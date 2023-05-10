class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        graph = defaultdict(list)
        for node1, node2 in edges:
            graph[node1].append(node2)
            graph[node2].append(node1)
        res = [0] * n
        def dfs(node, prev):
            count = Counter()
            label = labels[node]
            
            count[label] = 1
            
            for child in graph[node]:
                if child == prev:
                    continue
                count += dfs(child, node)
            res[node] = count[label]
            
            return count
        dfs(0, None)
        return res