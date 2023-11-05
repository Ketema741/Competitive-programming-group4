class Solution:
    def assignTasks(self, servers: List[int], tasks: List[int]) -> List[int]:
        res = [0] * len(tasks)
        available = [(weight, i) for i, weight in enumerate(servers)]
        heapq.heapify(available)
        unavailable = []

        time = 0
        for i in range(len(tasks)):
            time = max(time, i)

            if len(available) == 0:
                time = unavailable[0][0]
            
            while unavailable and time >= unavailable[0][0]:
                time_framme, weight, index = heapq.heappop(unavailable)
                heapq.heappush(available, (weight, index))
            
            weight, index = heapq.heappop(available)
            res[i] = index
            heapq.heappush(unavailable, (time + tasks[i], weight, index))
        
        return res