class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        graph = defaultdict(list)
        for i in range(len(edges)):
            src, dst = edges[i]
            
            graph[src].append([dst, succProb[i]])
            graph[dst].append([src, succProb[i]])
            
        queue= [(-1, start_node)]
        visited = set()
        
        while queue:
            prob, cur = heapq.heappop(queue)
            
            visited.add(cur)
            
            if cur == end_node:
                return prob * -1
            
            for nei, edgeProp in graph[cur]:
                if nei not in visited:
                    heapq.heappush(queue, (prob*edgeProp, nei))
                    
        return 0