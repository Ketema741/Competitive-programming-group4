# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        res = []
        
        def inorder(root):
            if root:
                inorder(root.left)
                res.append(root.val)
                inorder(root.right)
                
        inorder(root)  
        print(res)
        for i in range(1, len(res)):
            if res[i] <= res[i-1]:
                return False
            
        return True
        
"""         def valid(node, min_, max_):
            if not node:
                return True
            if  not (min_ < node.val < max_):
                return False
            
            min_ = valid(node.left, min_, node.val)
            max_ = valid(node.right, node.val, max_)
            
            return min_ and max_
        
        return valid(root, float('-inf'), float('inf'))
"""  
