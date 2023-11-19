def detect_negative_cycle(nodes, edges, graph):
    dist = [float('inf')] * nodes
    parent = [-1] * nodes

    for source in range(nodes):
        dist[source] = 0
        for _ in range(nodes - 1):
            for src, dst, weight in graph:
                if dist[src] + weight < dist[dst]:
                    dist[dst] = dist[src] + weight
                    parent[dst] = src

    for src, dst, weight in graph:
        if dist[src] + weight < dist[dst]:
            start_node = src
            cycle = [start_node]
            current = parent[start_node]

            while current != start_node:
                cycle.append(current)
                current = parent[current]

            cycle.append(start_node)
            return cycle

    return None

nodes, edges = map(int, input().split())
graph = []

for _ in range(edges):
    src, dst, weight = map(int, input().split())
    graph.append((src - 1, dst - 1, weight))

cycle = detect_negative_cycle(nodes, edges, graph)

if cycle is None:
    print("NO")
else:
    print("YES")
    print(" ".join(str(node + 1) for node in cycle))
