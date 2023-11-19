from collections import defaultdict, deque


test_len = int(input())
for _ in range(test_len):
    empty_line = input()
    n, k = list(map(int, input().split()))
    graph = defaultdict(list)
    inDegree = [0] * (n)

    for i in range(n-1):
        u, v = list(map(int, input().split()))
        u -= 1
        v -= 1
        graph[v].append(u)
        graph[u].append(v)
        inDegree[u] += 1
        inDegree[v] += 1

    queue = deque([])

    count = 0
    for i in range(n):
        if inDegree[i] == 1:
            queue.append((i, 1))
            count += 1

    while queue:
        
        node, opp = queue.popleft()

        for child in graph[node]:
            inDegree[child] -= 1
            if inDegree[child] == 1 and opp < k:
                count += 1
                queue.append((child, opp + 1))
                
    print(len(graph) - count)

