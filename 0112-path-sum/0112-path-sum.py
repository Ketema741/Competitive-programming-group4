# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def inorderDFS(node, curSum):
            if not node:
                return False
            curSum += node.val
            if not node.left and not node.right:
                return targetSum == curSum
            
            left = inorderDFS(node.left, curSum)
            right = inorderDFS(node.right, curSum)
            return left or right
        return inorderDFS(root, 0)
            