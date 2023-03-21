# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        count = 0
        hash_map = {0:1}
        def dfs(root, hash_map, curr_sum):
            nonlocal count

            if not root:
                return 
            
            sum_ = curr_sum + root.val   
            
            count += hash_map.get((sum_ - targetSum), 0)
            
            hash_map[sum_] = 1 + hash_map.get(sum_, 0)
                
            dfs(root.left, hash_map, sum_)
            dfs(root.right, hash_map, sum_)
            
            hash_map[sum_] -= 1
            if hash_map[sum_] == 0:
                hash_map.pop(sum_)
            
        dfs(root, hash_map, 0)
        return count
        