# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        res = []
        path = []
        
        def backtrack(root):
            if not root:
                return
            
            path.append(str(root.val))
                
            if not root.left and not root.right:
                res.append('->'.join(path))
                path.pop()
                return
              
           

            backtrack(root.left)
            backtrack(root.right)
            path.pop()
            
        backtrack(root)
        
        return res

        