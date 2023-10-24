# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        max_level = -1
        def dfs(root, level):
            nonlocal max_level

            if not root:
                return
            
            if level > max_level:
                res.append(root.val)

            max_level = max(max_level, level)

            dfs(root.right, 1 + level)
            dfs(root.left, 1 + level)
        dfs(root, 0)
        
        return res