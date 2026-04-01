# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        res = 0

        def dfs(node):
            nonlocal res
            if not node:
                return 0
            
            leftPath = dfs(node.left)
            rightPath = dfs(node.right)

            path = 1
            if node.left and node.left.val == node.val + 1:
                path = max(path, 1 + leftPath)
            
            if node.right and node.right.val == node.val + 1:
                path = max(path, 1 + rightPath)
            
            res = max(res, path)
            return path
        
        dfs(root)
        return res