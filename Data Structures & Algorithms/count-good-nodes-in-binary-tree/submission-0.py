# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 0
        
        def isGood(node, maxValue): 
            if not node:
                return 
            print(f"node{node.val} -> {maxValue}")
            nonlocal res
            if node.val >= maxValue:
                print(f"node:{node.val}")
                res += 1
                maxValue = node.val
            if node.left: 
                isGood(node.left, maxValue)    
            if node.right:
                isGood(node.right, maxValue) 

        isGood(root, root.val)        
        return res 


        