# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        current1, current2 = list1, list2 
        ret = ListNode()
        current_r = ret
        while current1 and current2 :
            if current1.val < current2.val :
                current_r.next = current1 
                current1 = current1.next  
            else:
                current_r.next = current2 
                current2 = current2.next 
            current_r = current_r.next
        
        while current1:
            current_r.next = current1 
            current1 = current1.next  
            current_r = current_r.next

        while current2:
            current_r.next = current2
            current2 = current2.next  
            current_r = current_r.next     
 
        return ret.next
