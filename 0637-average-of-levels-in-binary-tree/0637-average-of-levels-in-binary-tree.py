# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        res = []

        queue = deque([root])
        level = 1
        while queue:
            sum_ = 0
            size = len(queue)

            for i in range(size):
                current = queue.popleft()
                sum_ += current.val
                
                if current.left:
                    queue.append(current.left)
                    
                if current.right:
                    queue.append(current.right)

            res.append(sum_/size)
            level += 1
                
        return res
                    

