# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        res = TreeNode(0)
        
        def dfs(original, cloned):
            if original:
                dfs(original.left, cloned.left)
                if original is target:
                    res.next = cloned
                dfs(original.right, cloned.right)
        dfs(original, cloned)
        return res.next