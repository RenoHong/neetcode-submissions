# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def isValid(node, min_value, max_value):
            if not node :
                return True 
            if min_value < node.val < max_value :
                return isValid(node.left, min_value, node.val) and isValid(node.right, node.val, max_value)
            else:
                return False

        return isValid(root, float('-inf'), float('inf'))
        
        