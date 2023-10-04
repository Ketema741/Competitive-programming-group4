class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)
        for start, dest, price in flights:
            graph[start].append((dest, price))
        
        prices = [float('inf') for i in range(n)]
        prices[src] = 0
        
        minHeap = [( 0, prices[src], src)]
        
        while minHeap:
            stops, total_cost, cur = heappop(minHeap)
            neighbours = graph[cur]
            
            for neighbour, cost in neighbours:
                if prices[neighbour] > total_cost + cost and stops <= k: 
                    prices[neighbour] = total_cost + cost
                    
                    heappush(minHeap, (stops + 1, prices[neighbour], neighbour))

        return prices[dst] if prices[dst] != float('inf') else -1