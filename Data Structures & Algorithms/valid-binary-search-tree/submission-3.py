# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        stack = [(root, -float('inf'), float('inf'))]

        while stack:
            node, minval, maxval = stack.pop()

            if not (minval < node.val < maxval):
                return False
            
            if node.right:
                stack.append((node.right, node.val, maxval))
            if node.left:
                stack.append((node.left, minval, node.val))
      
        return True