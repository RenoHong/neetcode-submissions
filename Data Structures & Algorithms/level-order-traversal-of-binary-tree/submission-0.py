# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ls = [] 
        level = 0
        def levelDFS(node, level, ls) -> None :
            if node:
                if len(ls) == level :
                    ls.append([])
                ls[level].append(node.val) 
                levelDFS(node.left, level +1, ls) 
                levelDFS(node.right, level+1, ls)
        levelDFS(root, level, ls)
        return ls   
        