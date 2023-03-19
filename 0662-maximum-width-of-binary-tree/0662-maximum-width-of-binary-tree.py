# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        queue = deque([(root, 0)])
        max_width = 1
        
        while queue:
            level_size = len(queue)
            level_start = level_end = 0
            
            for i in range(level_size):
                node, pos = queue.popleft()
                
                if i == 0:
                    level_start = pos
                
                if i == level_size - 1:
                    level_end = pos
                
                if node.left:
                    queue.append((node.left, pos*2))
                    
                if node.right:
                    queue.append((node.right, pos*2 + 1))
            
            width = level_end - level_start + 1
            max_width = max(max_width, width)
        
        return max_width
