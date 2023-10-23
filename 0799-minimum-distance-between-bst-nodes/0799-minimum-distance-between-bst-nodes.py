# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        res = float("inf")
        prev = None

        def dfs(root):
            nonlocal res, prev
            if not root:
                return

            dfs(root.left)
            if prev:
                res = min(res, root.val - prev.val)
            prev = root

            dfs(root.right)

        dfs(root)

        return res