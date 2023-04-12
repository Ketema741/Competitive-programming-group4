class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visited = set()
    
        def dfs(province):
            visited.add(province)
            for neighbour in graph[province]:
                if neighbour not in visited:
                    dfs(neighbour)

        graph = defaultdict(list)
        for row in range(len(isConnected)):
            for col in range(len(isConnected[0])):
                if isConnected[row][col] == 1:
                    graph[row+1].append(col+1)
        count = 0
        for province in graph.keys():
            if province not in visited:
                count += 1
                dfs(province)

        return count