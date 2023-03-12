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
            
            # base case
            if not root:
                return
            
            # check if results is found
            if not root.left and not root.right:
                current_path.append(str(root.val))
                res.append('->'.join(current_path))
                current_path.pop() 
                return 
            
            for i in range(2):
                current_path.append(str(root.val)) # choose

                # explore left  or right path
                if i == 1: 
                    backtrack(root.left) 
                else: 
                    backtrack(root.right)
                    
                current_path.pop() # unchoose
            
        backtrack(root)
        
        return res