# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        
        def insert(root, val):
            if not root.right and root.val < val:
                newNode = TreeNode(val)
                root.right = newNode
                return
            
            if not root.left and root.val > val:
                newNode = TreeNode(val)
                root.left = newNode
                return
        
            if val < root.val:
                return insert(root.left, val)
            if val > root.val:
                return insert(root.right, val)
        
        if not root:
            root = TreeNode(val)
        else:
            insert(root, val)
            
        return root