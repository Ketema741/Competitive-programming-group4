# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from typing import List

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res = []

        def dfs(node, curSum, curPath):
            if not node:
                return

            curSum -= node.val
            curPath.append(node.val)

            if not node.left and not node.right and curSum == 0:
                res.append(curPath[:])

            dfs(node.left, curSum, curPath)
            dfs(node.right, curSum, curPath)

            curPath.pop()

        dfs(root, targetSum, [])
        return res
