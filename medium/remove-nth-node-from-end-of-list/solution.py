# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        current = head
        prev = head
        
        
        for i in range(n):
            current = current.next
            
        
        # if n == len(list_node)
        if current == None:
            return head.next
        
                
        while current.next != None:
            current = current.next
            prev = prev.next
        
        prev.next = prev.next.next
        return head
