# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        root = TreeNode(preorder[0])
        stack = [root]
        
        for value in preorder[1:]:
            node = TreeNode(value)
            
            if value < stack[-1].val:
                stack[-1].left = node 
                stack.append(stack[-1].left)
            else:
                while stack and value > stack[-1].val:
                    last = stack.pop()
                last.right = node
                stack.append(last.right)
    
    
        return root
    
    
    
    """
        def bfs(preorder, size):
            if not preorder:
                return None

            end = 1
            while end < size and preorder[0] > preorder[end]:
                    end += 1

            left_subtree = preorder[1:end]
            right_subtree = preorder[end:]

            root = TreeNode(preorder[0])

            root.left = bfs(left_subtree, len(left_subtree))
            root.right = bfs(right_subtree, len(right_subtree))
            return root
                
        return bfs(preorder, len(preorder))
        
        """