# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        
        counter = 0
        
        p = head
        while p != None:
            counter += 1
            p = p.next
            
    
        pp = head
        sums =  0
        while counter != 0:
            
            if pp.val == 1:
                sums += 2**(counter-1)
            
            counter -= 1
            pp = pp.next
        
        return sums
            
