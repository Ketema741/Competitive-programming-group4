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
            nodes_len = [0]
            
            for i in range(len(node.children)):
                nodes_len.append(dfs(node.children[i]))
            
            
            return  1 + max(nodes_len)
        return dfs(root)