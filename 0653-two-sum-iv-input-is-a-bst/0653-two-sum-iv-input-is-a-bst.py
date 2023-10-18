# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        
        queue = deque([root])

        hash_map = defaultdict(int)

        while queue:
            node = queue.popleft()
            diff = k - node.val

            if diff in hash_map:
                return True

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
                
            hash_map[node.val] = 1

        return False