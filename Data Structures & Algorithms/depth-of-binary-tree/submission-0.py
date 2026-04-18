# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.maxNDepth(root, 0)

    def maxNDepth(self, root, level):
        if not root: 
            return level
        
        return max(self.maxNDepth(root.left, level +1), self.maxNDepth(root.right, level+1))