# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or len(preorder) == 0 :
            return None

        index_map = {key: i for i, key in enumerate(inorder)} 

        def build(left_pre, right_pre, left_in, right_in):
            if left_pre > right_pre :
                return None
            root = TreeNode(preorder[left_pre])

            in_root_index = index_map[root.val]

            left_size = in_root_index - left_in
            
            root.left = build(left_pre +1 , left_pre + left_size, left_in, in_root_index -1)
            root.right = build(left_pre + left_size +1, right_pre, in_root_index + 1, right_in)
            return root 
        return build(0, len(preorder) -1 , 0, len(inorder) -1)
            

                 