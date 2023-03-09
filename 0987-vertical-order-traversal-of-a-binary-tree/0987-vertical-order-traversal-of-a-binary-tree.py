# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = deque([(root, 0, 0)])
        node_list = []
        
        while queue:
            node, row, col = queue.popleft()
            if node:
                node_list.append((col, row, node.val))
                queue.append((node.left, row+1, col-1))
                queue.append((node.right, row+1, col+1))
        
        node_list.sort()
        col_dict = {}
        for col, row, val in node_list:
            if col not in col_dict:
                col_dict[col] = [(row, val)]
            else:
                col_dict[col].append((row, val))
        
        res = []
        for col in col_dict:
            res.append([val for row, val in sorted(col_dict[col], key=lambda x: (x[0], x[1]))])
        
        return res