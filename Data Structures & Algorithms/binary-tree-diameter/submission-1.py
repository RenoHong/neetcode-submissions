# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_diameter = 0 

        def dfs(node):
            if not node : return 0 

            h_left = dfs(node.left) 
            h_right = dfs(node.right) 

            self.max_diameter = max(self.max_diameter, h_left + h_right) 

            return max(h_left , h_right) + 1
        
        dfs(root)
        return self.max_diameter
        