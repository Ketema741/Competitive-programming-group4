# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        self.res = 0

        def dfs(root, low, high):
            if not root:
                return
            if low <= root.val <= high:
                self.res += root.val

            dfs(root.left, low, high)
            dfs(root.right, low, high)

        dfs(root, low, high)
        return self.res