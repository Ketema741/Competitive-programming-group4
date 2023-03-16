# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        path_sum = -inf
        
        def subtreeGain(root):
            nonlocal path_sum
            
            if not root:
                return 0
            
            left_gain = max(subtreeGain(root.left), 0)
            right_gain = max(subtreeGain(root.right), 0)
            
            path_sum = max(path_sum, root.val + left_gain + right_gain)
            
            return max(root.val + left_gain, root.val + right_gain)
        
        subtreeGain(root)
        
        return path_sum