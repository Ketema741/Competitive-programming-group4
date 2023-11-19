from collections import defaultdict


t = int(input())

for _ in range(t):
    n, m = list(map(int, input().split()))
    graph = defaultdict(list)
    indegree = [0 for i in range(n)]
    
    for _ in range(m):
        u, v = list(map(int, input().split()))
        graph[u].append(v)
        graph[v].append(u)
        indegree[u-1] +=  1
        indegree[v-1] +=  1

    leaf = 0
    for i in indegree:
        if i == 1:
            leaf += 1
    x = n -(leaf + 1)
    y = leaf//x

    print(*[x, y])



    
    
    
    