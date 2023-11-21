class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        for i, task in enumerate(tasks): #O(N)
            task.append(i)

        tasks.sort()
        res, available_tasks = [], []
        i, time = 0, tasks[0][0]

        
        while available_tasks or i < len(tasks): # O(N)
            while i < len(tasks) and time >= tasks[i][0]:
                heapq.heappush(available_tasks, [tasks[i][1], tasks[i][2]]) # O(log(N))
                i += 1
            
            if not available_tasks:
                time = tasks[i][0] # skip idle time
            else:
                proces_time, index = heapq.heappop(available_tasks)
                time += proces_time
                res.append(index)

        return res