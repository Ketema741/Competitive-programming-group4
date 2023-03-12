# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        res, current_path = [], []
        
        def backtrack(root):
            if not root:
                return
            
        
            if not root.left and not root.right:
                current_path.append(str(root.val))
                res.append('->'.join(current_path))
                current_path.pop()
                return 
            
            current_path.append(str(root.val))
            backtrack(root.left)
            backtrack(root.right)
            current_path.pop()
            
        backtrack(root)
        
        return res

        