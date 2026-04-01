# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        stack = [(p, q)]

        while stack:
            l, r = stack.pop()
            # Check the base case:
            if not l and not r:
                continue
            if not l or not r or l.val != r.val:
                return False
            
            stack.append((l.left, r.left))
            stack.append((l.right, r.right))
        
        return True