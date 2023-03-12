# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        res, current_path = [], []
        
        def dfs(root):
            
            # check if results is found
            if not root.left and not root.right:
                res.append('->'.join(current_path + [str(root.val)]))
                return 
            
            current_path.append(str(root.val)) #choose
            # explore
            if root.left:
                dfs(root.left)
            if root.right:
                dfs(root.right)
                
            current_path.pop() # unchoose
            
        dfs(root)
        
        return res