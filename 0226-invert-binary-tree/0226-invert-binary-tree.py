# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        dummy = root
        
        def invertNode(root):
            if not root:
                return None
            
            left = invertNode(root.left)
            right = invertNode(root.right)
            
            root.left = right
            root.right = left
            return root
        
        invertNode(root)
        return dummy