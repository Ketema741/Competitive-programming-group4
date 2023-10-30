# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        hashMap = defaultdict(list)
        res = []

        def dfs(node):
            if not node:
                return "null"
            
            s = ','.join([str(node.val), dfs(node.left), dfs(node.right)])

            if len(hashMap[s]) == 1:
                res.append(node)
            
            hashMap[s].append(node)

            return s

        dfs(root)
        return res