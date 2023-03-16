# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0
        
        def postOrder(root, max_):
            if not root:
                return 0
            
            left = postOrder(root.left, max(max_, root.val))
            right = postOrder(root.right, max(max_, root.val))
            
            if root.val >= max_:
                return 1 + left + right
            return left + right
        
        return postOrder(root, -inf)