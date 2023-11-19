class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        if n == 0:
            return len(tasks)

        maxHeap = [-cnt for cnt in Counter(tasks).values()]
        queue = deque([])
    
        heapq.heapify(maxHeap)
        times = 0

        while queue or maxHeap:
            times += 1 

            if maxHeap:
                cnt = 1 + heapq.heappop(maxHeap)

                if cnt:
                    queue.append([cnt, times + n])

            if queue and queue[0][1] == times:
                heapq.heappush(maxHeap, queue.popleft()[0])
                
        return times
            
        
        