# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        arr = [] 
        for list in lists :
            node = list
            while node:
                arr.append(node.val)
                node = node.next

            
        arr.sort()
        res = ListNode()
        curr = res
        for i in arr:
            curr.next = ListNode(i)
            curr = curr.next 
        
        return res.next 
                        

