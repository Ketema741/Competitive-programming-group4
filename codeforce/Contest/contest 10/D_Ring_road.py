from collections import defaultdict


n = int(input())
graph = defaultdict(list)
graph_cost = defaultdict()

tot_cost = 0

for _ in range(n):
    node1, node2, cost = list(map(int, input().split()))
    
    graph[node1].append(node2)
    graph[node2].append(node1)

    graph_cost[(node1, node2)] = 0
    graph_cost[(node2, node1)] = cost

    tot_cost += cost


cycle = [1]
cycle.append(graph[1][0])


while len(cycle) < n:
    node = cycle[-1]
    if graph[node][0] != cycle[-2]:
        cycle.append(graph[node][0])
    else:
        cycle.append(graph[node][1])


min_cost = 0
for i in range(n):
    min_cost += graph_cost[(cycle[i-1], cycle[i])]

if tot_cost - min_cost < min_cost:
    print(tot_cost - min_cost)
else:
    print(min_cost)