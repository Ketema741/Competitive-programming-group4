class Solution:
    def numTrees(self, n: int) -> int:
        numTree = [1] * (n + 1)

        for nodes in range(2, n + 1):
            tot = 0

            for root in range(1, nodes + 1):
                left = numTree[root - 1]
                right = numTree[nodes - root]
                tot += left * right

            numTree[nodes] = tot

        return numTree[n]