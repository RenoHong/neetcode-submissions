# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = fast = head
        if not fast or not fast.next or not fast.next.next:
            return False

        slow = slow.next 
        fast = fast.next.next
        while fast and fast.next and fast.next.next:
            if fast == slow :
                print(f"{fast} -> {slow}")
                return True
            fast = fast.next.next
            slow = slow.next
        return False