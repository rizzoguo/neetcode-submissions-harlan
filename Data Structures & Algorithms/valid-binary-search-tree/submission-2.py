# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        q = deque([(root, -float('inf'), float('inf'))])
        while q:
            node, minval, maxval = q.popleft()
            if node.left:
                if minval < node.left.val < node.val:
                    q.append((node.left, minval, node.val))
                else:
                    return False
            if node.right:
                if node.val < node.right.val < maxval:
                    q.append((node.right, node.val, maxval))
                else:
                    return False
        
        return True