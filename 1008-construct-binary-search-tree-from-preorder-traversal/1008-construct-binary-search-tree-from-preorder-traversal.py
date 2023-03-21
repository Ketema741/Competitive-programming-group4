# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bfs(self, preorder, size):
        if not preorder:
            return None
            
        end = 1
        while end < size and preorder[0] > preorder[end]:
                end += 1
            
        left_subtree = preorder[1:end]
        right_subtree = preorder[end:]
            
        root = TreeNode(preorder[0])
            
        root.left = self.bfs(left_subtree, len(left_subtree))
        root.right = self.bfs(right_subtree, len(right_subtree))
        return root
        
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
                
        return self.bfs(preorder, len(preorder))