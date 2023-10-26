class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        graph = defaultdict(list)

        for i in range(n):
            graph[manager[i]].append(i)

        q = deque([(headID, 0)])
        res = 0
        
        while q:
            node, time = q.popleft()
            res = max(res, time)

            for nei in graph[node]:
                q.append((nei, time + informTime[node]))
        
        return res