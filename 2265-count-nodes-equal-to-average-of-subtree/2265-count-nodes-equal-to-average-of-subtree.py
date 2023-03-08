# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        count = 0
        def dfs(root):
            nonlocal count
            if not root:
                return [0, 0]
            
            left = dfs(root.left)
            right = dfs(root.right)
            
            sum_ = root.val + left[0] + right[0]
            nodes_num = 1 + left[1] + right[1]
            average = sum_ // nodes_num
            
            if average == root.val:
                count += 1
            return [sum_, nodes_num]
        dfs(root)
        return count
            
            