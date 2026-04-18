# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        self.sum = float('-inf')

        def gain(node) :

            if not node:
                return 0  

            gain_left = gain(node.left)
            gain_right = gain(node.right)
            
            the_max = max(node.val+ gain_left, node.val+ gain_right, node.val+ gain_left + gain_right, node.val)
            self.sum = max(the_max, self.sum)

            return max(node.val+ gain_left, node.val+ gain_right, node.val)

        gain(root)
        return self.sum 
      