# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        def dfs(root):
            if not root:
                return 0
                
            left = dfs(root.left)
            right = dfs(root.right)
            
            self.res += left if left >= 0 else -1*left
            self.res += right if right >= 0 else -1*right

            return root.val - 1 + left + right
        
        dfs(root)

        return self.res
