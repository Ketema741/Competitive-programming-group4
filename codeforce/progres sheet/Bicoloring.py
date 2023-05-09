from collections import defaultdict


def main():
    def dfs(node, color):
        if colors[node] != -1:
            return colors[node] == color

        colors[node] = color

        for neighbor in adj_list[node]:
            if not dfs(neighbor, 1 - color):
                return False

        return True

    while True:
        n = int(input())
        if n == 0:
            break

        l = int(input())
        adj_list = defaultdict(list)
        colors = [-1] * n

        for i in range(l):
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
