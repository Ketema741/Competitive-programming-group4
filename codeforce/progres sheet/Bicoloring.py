from collections import defaultdict


def main():
    def dfs(node, color):
        if colors[node] != -1:
            return colors[node] == color

        colors[node] = color

        for child in adj_list[node]:
            if not dfs(child, 1 - color):
                return False

        return True

    while True:
        nodes = int(input())
        if nodes == 0:
            break

        edges = int(input())
        adj_list = defaultdict(list)
        colors = [-1] * nodes

        for _ in range(edges):
            node1, node2 = map(int, input().split())
            adj_list[node1 - 1].append(node2 - 1)
            adj_list[node2 - 1].append(node1 - 1)

        is_bicolorable = dfs(0, 0)
        if is_bicolorable:
            print("BICOLOURABLE.")
        else:
            print("NOT BICOLOURABLE.")


if __name__ == '__main__':
    main()
