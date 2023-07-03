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