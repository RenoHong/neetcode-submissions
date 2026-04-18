# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
         
        lres = ListNode(0)
        p = lres
        remain = 0 
        while l1 and l2:
            lres.next = ListNode((l1.val + l2.val + remain) %10)
            remain = (l1.val + l2.val + remain) // 10
            l1 = l1.next 
            l2 = l2.next
            lres = lres.next

        while l1:
            lres.next = ListNode((l1.val + remain)%10)
            remain = (l1.val + remain) // 10
            l1 = l1.next 
            lres = lres.next 

        while l2:
            lres.next = ListNode((l2.val + remain)%10)
            remain = (l2.val + remain) // 10
            l2 = l2.next 
            lres = lres.next      

        if remain > 0 :
            lres.next = ListNode(remain)  
        
        return p.next