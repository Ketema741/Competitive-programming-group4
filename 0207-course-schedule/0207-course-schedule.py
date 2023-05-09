class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        incoming = [0] * numCourses
        res = []
        for post, pre in prerequisites:
            graph[pre].append(post)
            incoming[post] += 1
        queue = deque([])
        
        for i in range(numCourses):
            if incoming[i] == 0:
                queue.append(i)
        
        while queue:
            node = queue.popleft()
            res.append(node)
            
            for neighbor in (graph[node]):
                incoming[neighbor] -= 1
                
                if incoming [neighbor] == 0:
                    queue.append(neighbor)
        if len(res) != numCourses:
            return False
        
        return True