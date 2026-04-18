# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def height(node):
            if not node : return  0

            h_left = height(node.left)
            h_right = height(node.right)

            if h_left == -1 or h_right == -1 : return  -1
            if abs(h_left - h_right) > 1 : return -1

            return max(h_left, h_right) + 1

        return height(root) != -1



