# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        stack = [root]
        # map[node] = (height, diameter) for subtree rooted at node
        mp = {None: (0, 0)}

        while stack:
            node = stack[-1]
            # Postorder simulation: ensure processed children before parents
            if node.left and node.left not in mp:
                stack.append(node.left)
            elif node.right and node.right not in mp:
                stack.append(node.right)
            
            else:
                node = stack.pop()
                leftheight, leftdiameter = mp[node.left]
                rightheight, rightdiameter = mp[node.right]

                mp[node] = (1 + max(leftheight, rightheight), 
                # Diameter candidates:
                #1: path through the node: leftHeight + rightHeight
                #2: best entirely in left subtree: leftDiameter
                #3: best entirely in right subtree: rightDiameter
                max(leftheight + rightheight, leftdiameter, rightdiameter))
        
        return mp[root][1]