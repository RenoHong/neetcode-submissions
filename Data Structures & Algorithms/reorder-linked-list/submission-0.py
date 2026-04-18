# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head:
            return None
        
        slow = fast = head 
        while fast and fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next  

        # reset back to mid
        fast = slow.next 
        pre = slow
        slow.next = None

        while fast:
            next = fast.next 
            fast.next = pre
            pre = fast 
            fast = next
        
        p =  head 
        preNext = pre
        while p != slow:
            next = p.next
            p.next = pre
            preNext = pre.next
            pre.next = next
            p = next
            pre= preNext

        if preNext:
            p.next = preNext
            preNext.next = None 
 
        # print(head)