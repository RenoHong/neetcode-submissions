# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        ls = []
        if root:
            q = deque()
            q.append(root)
            ls.append(str(root.val))

            while q:
                node = q.popleft()  
                if node.left:
                    q.append(node.left) 
                    ls.append(str(node.left.val))
                else:
                    ls.append('None')
                
                if node.right:
                    q.append(node.right)
                    ls.append(str(node.right.val))
                else:
                    ls.append('None')

            return ','.join(ls)
        return ""
 



        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if len(data) == 0 :
            return None
        
        self.ls = data.split(",") 
        q = deque()
        root = TreeNode(self.ls[0])
        q.append(root)
        index = 0 
        while q:
            node = q.popleft()

            index += 1
            s = self.ls[index]
            if s == 'None':
                node.left = None 
            else:
                node.left = TreeNode(int(s))
                q.append(node.left)
            
            index += 1
            s = self.ls[index]
            if s == 'None':
                node.right = None 
            else:
                node.right = TreeNode(int(s))
                q.append(node.right)

        return root

            
