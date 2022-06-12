# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        p = head
        total_len = 0
        while (p != None):
            p = p.next
            total_len += 1
            
        
        
        pp = head
        idx = 0
        while (idx < total_len // 2):
            idx += 1
            pp = pp.next
            
        return pp
