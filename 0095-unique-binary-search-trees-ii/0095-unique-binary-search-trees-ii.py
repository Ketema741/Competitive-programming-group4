# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        
        def generate(l, r):
            if l == r:
                return [TreeNode(l)]

            if l > r:
                return [None]

            res = []
            for val in range(l, r + 1):
                leftTrees = generate(l, val - 1)
                rightTrees = generate(val + 1, r)

                for leftTree in leftTrees:
                    for rightTree in rightTrees:
                        root = TreeNode(val, leftTree, rightTree)
                        res.append(root)

            return res

        return generate(1, n)