class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        reverseGraph = defaultdict(list)
        outDegree = [0] * len(graph)

        for i in range(len(graph)):
            for j in graph[i]:
                reverseGraph[j].append(i)
                outDegree[i] += 1

        queue = deque()
        for i in range(len(outDegree)):
            if outDegree[i] == 0:
                queue.append(i)

        res = []
        while queue:
            node = queue.popleft()
            res.append(node)
            for parent in reverseGraph[node]:
                outDegree[parent] -= 1
                if outDegree[parent] == 0:
                    queue.append(parent)

        res.sort()
        return res
