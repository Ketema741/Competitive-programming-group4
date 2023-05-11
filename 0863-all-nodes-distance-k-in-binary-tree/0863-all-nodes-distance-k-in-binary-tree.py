# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        graph = defaultdict(list)
        
        def build(node):
            if not node: return
            
            if node.left:
                graph[node.val].append(node.left.val)
                graph[node.left.val].append(node.val)
                
            if node.right:
                graph[node.val].append(node.right.val)
                graph[node.right.val].append(node.val)
                
            build(node.left)
            build(node.right)
            
        build(root)
        queue = deque([])

        queue.append((target.val, 0))
        
        visited = set()
        visited.add(target.val)
        res = []

        while queue:
            node, distance = queue.popleft()

            if distance == k:
                res.append(node)
                

            for child in graph[node]:
                if child not in visited:
                    queue.append((child, distance + 1))
                    visited.add(node)

        return res