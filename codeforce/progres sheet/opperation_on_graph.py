from collections import defaultdict


n = int(input())

k = int(input())

matrix = defaultdict(list)

for _ in range(k):
    opp = list(map(int, input().split()))

    if opp[0] == 1:
        u, v= opp[1], opp[2]
        matrix[u].append(v)
        matrix[v].append(u)
    else:
        vertex = opp[1]
        print(*matrix[vertex])