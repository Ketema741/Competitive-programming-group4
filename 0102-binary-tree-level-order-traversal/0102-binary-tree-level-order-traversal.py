# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        
        queu = deque([])
        queu.append(root)
        if not root:
            return res
        while queu:
            size = len(queu)
            temp = []
            for i in range(size):
                current = queu.popleft()
                temp.append(current.val)
                if current.left:
                    queu.append(current.left)
                if current.right:
                    queu.append(current.right)
            res.append(temp)
            
        return res