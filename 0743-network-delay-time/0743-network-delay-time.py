class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        
        for src, dst, cost in times:
            graph[src].append((dst, cost))
        
        minHeap = [(0, k)] #(const, startNode)
        visited = set()
        maxCost = 0
        
        while minHeap:
            cost, node = heapq.heappop(minHeap)
            
            if node in visited:
                continue
                
            maxCost =  cost
            visited.add(node)
            
            neighbours = graph[node]
            
            for neighbour in neighbours:
                newNode,  newCost = neighbour
               
                
                if newNode not in visited:
                    currCost = cost +  newCost
                    heapq.heappush(minHeap, (currCost, newNode))
                    
        return maxCost if len(visited) == n else -1