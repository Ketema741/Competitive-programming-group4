# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_hash_map = {}
        for i, num in enumerate(inorder):
            inorder_hash_map[num] = i
            
        def listToTree(preorder, inorder):
            if not preorder and not inorder:
                return None

            root = TreeNode(preorder[0])

            mid = inorder_hash_map[preorder[0]]
            
            root.left = self.buildTree(preorder[1:mid+1], inorder[:mid])
            root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])
            
            return root
        
        return listToTree(preorder, inorder)