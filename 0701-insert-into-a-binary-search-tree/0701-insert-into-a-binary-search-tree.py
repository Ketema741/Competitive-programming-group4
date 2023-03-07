# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        node = root
        
        def insert(root, val):
            if root.right == None and root.val < val:
                newNode = TreeNode(val)
                root.right = newNode
                return
            if root.left == None and root.val > val:
                newNode = TreeNode(val)
                root.left = newNode
                return
                
            
            if val < root.val:
                return insert(root.left, val)
            if val > root.val:
                return insert(root.right, val)
        if not root:
            newNode = TreeNode(val)
            root = newNode
        else:
            insert(node, val)
        return root