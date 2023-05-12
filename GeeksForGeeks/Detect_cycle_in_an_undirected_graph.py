from typing import List
from collections import deque


class Solution:
    # Function to detect cycle in an undirected graph.
    def isCycle(self, V: int, adj: List[List[int]]) -> bool:
        inDegree = [0] * V

        for i, childs in enumerate(adj):
            inDegree[i] = len(childs)

        queue = deque([])

        for i in range(V):
            if inDegree[i] <= 1:
                queue.append(i)
        res = []

        while queue:
            node = queue.popleft()
            res.append(node)

            for child in adj[node]:
                inDegree[child] -= 1
                if inDegree[child] == 1:
                    queue.append(child)
        return len(res) != V


# {
 # Driver Code Starts
if __name__ == '__main__':

    T = int(input())
    for i in range(T):
        V, E = map(int, input().split())
        adj = [[] for i in range(V)]
        for _ in range(E):
            u, v = map(int, input().split())
            adj[u].append(v)
            adj[v].append(u)
        obj = Solution()
        ans = obj.isCycle(V, adj)
        if (ans):
            print("1")
        else:
            print("0")

# } Driver Code Ends
