# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = [] 
        rows = []
        def BFS(node, level, rows):
            if node:
                if len(rows) == level :
                    rows.append([])
                rows[level].append(node.val)

                if node.left:
                    BFS(node.left, level +1, rows)
                if node.right:
                    BFS(node.right, level+1, rows)
        BFS(root, 0, rows)        
        for r in rows:
            res.append(r[-1]) 

        return res
