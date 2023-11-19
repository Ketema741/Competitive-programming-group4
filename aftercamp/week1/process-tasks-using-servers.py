class Solution:
    def assignTasks(self, servers: List[int], tasks: List[int]) -> List[int]:
        res = [0] * len(tasks)
        available = [(weight, i) for i, weight in enumerate(servers)]
        heapq.heapify(available) # O(N)
        unavailable = []

        time = 0
        for task in range(len(tasks)):
            time = max(time, task)

            # waiting until at leas one server is available
            if len(available) == 0:
                time = unavailable[0][0]
            
            while unavailable and time >= unavailable[0][0]:
                end_time, weight, server = heapq.heappop(unavailable)
                heapq.heappush(available, (weight, server))
            
            weight, server = heapq.heappop(available)
            res[task] = server
            heapq.heappush(unavailable, (time + tasks[task], weight, server))
        
        return res