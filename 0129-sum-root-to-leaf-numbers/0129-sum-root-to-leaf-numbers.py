class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        res = []
        
        def dfs(node, path):
            if not node.left and not node.right:
                string = ''.join(path) + str(node.val)
                res.append(string)
                return
            
            if node.left:
                dfs(node.left, path + [str(node.val)])
            if node.right:
                dfs(node.right, path + [str(node.val)])
            
        dfs(root, [])
        
        return sum([int(num) for num in res])
