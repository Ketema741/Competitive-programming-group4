class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph = defaultdict(list)
        
        for src, dst in prerequisites:
            graph[src].append(dst)

        def hasPath(start, dst):
            visited = set()
            queue = [(0, start)]

            while queue:
                cost, node = heapq.heappop(queue)

                if node in visited:
                    continue

                visited.add(node)

                if node == dst:
                    return True

                for neighbor in graph[node]:
                    if neighbor not in visited:
                        heapq.heappush(queue, (cost + 1, neighbor))

            return False

        answer = []

        for src, dst in queries:
            answer.append(hasPath(src, dst))

        return answer