# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = deque([])
        res = []
        if root:
            queue.append(root)
            
        level = 0  
        while queue:
            temp = []

            for _ in range(len(queue)):
                node = queue.popleft()
                temp.append(node.val)
                
                if node.left:
                    queue.append(node.left)
                    
                if node.right:
                    queue.append(node.right)
                    
            if level % 2 != 0:
                res.append(temp[::-1])
            else:
                res.append(temp)
                
            level += 1
            
        return res