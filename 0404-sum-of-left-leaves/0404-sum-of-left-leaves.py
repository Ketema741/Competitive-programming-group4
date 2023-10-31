# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        def isLeaf(node):
            return node and not node.left and not node.right

        res = 0

        if not root:
            return res

        q = deque([root])

        while q:
            node = q.popleft()

            if isLeaf(node.left):
                res += node.left.val

            if node.left:
                q.append(node.left)

            if node.right:
                q.append(node.right)

        return res
