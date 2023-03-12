# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def valid(node, min_, max_):
            if not node:
                return True
            if  not (min_ < node.val < max_):
                return False
            
            min_ = valid(node.left, min_, node.val)
            max_ = valid(node.right, node.val, max_)
            
            return min_ and max_
        
        return valid(root, float('-inf'), float('inf'))
