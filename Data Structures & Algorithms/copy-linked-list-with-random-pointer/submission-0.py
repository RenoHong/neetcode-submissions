"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
 
        temp = head 
        while temp:
            next_node = temp.next
            temp.next = Node(temp.val)
            temp.next.next = next_node 
            temp = next_node
        
        temp = head 
        while temp:
            r = temp.random
            if r:
                temp.next.random = r.next
            temp = temp.next.next
        

        curr = head
        res = head.next
        while curr :
            temp = curr.next 
            curr.next = temp.next  
            if temp.next:
                temp.next = temp.next.next
            curr = curr.next

        return res 