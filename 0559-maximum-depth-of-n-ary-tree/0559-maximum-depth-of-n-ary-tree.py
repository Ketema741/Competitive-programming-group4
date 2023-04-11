"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
        
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        
        def dfs(node):
            if not node:
                return 0
            
            max_child_height = 0
            
            for i in range(len(node.children)):
                max_child_height = max(max_child_height, dfs(node.children[i]))
            
            return  1 + max_child_height
        
        return dfs(root)