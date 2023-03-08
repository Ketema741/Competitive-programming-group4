# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        ans = []
        def inorder(root):
            if not root:
                return 
            
            inorder(root.left)
            res.append(root.val)
            inorder(root.right)
        inorder(root)
        res = Counter(res)
        res = sorted(res.items(), key = lambda x: x[1])
        print(res)
        end = len(res) - 1
        ans.append(res[end][0])
        for i in range(end-1, -1, -1):
            if res[i+1][1] != res[i][1]:
                break
            ans.append(res[i][0])
        return ans