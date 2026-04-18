# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        t = k 
        curr = head
        while t > 0:
            if not curr:
                return head
            curr = curr.next 
            t -= 1

        t = k 
        curr = head
        pre = None
        while t > 0 :
            next_node = curr.next 
            curr.next = pre
            pre = curr 
            curr = next_node
            t -= 1
        head.next  = self.reverseKGroup(curr, k)
        return pre

        
        